"""
Sparse-sampling reconstruction methods.
"""

import numpy as np
from scipy.interpolate import RBFInterpolator, griddata


def random_mask(shape, fraction, random_state=42):
    """
    Generate a boolean sampling mask with `fraction` of pixels True.

    Parameters
    ----------
    shape : tuple  (n_x, n_y)
    fraction : float  in (0, 1]
    """
    rng = np.random.default_rng(random_state)
    n_total = shape[0] * shape[1]
    n_sample = max(4, int(fraction * n_total))
    idx = rng.choice(n_total, n_sample, replace=False)
    mask = np.zeros(n_total, dtype=bool)
    mask[idx] = True
    return mask.reshape(shape)


def grid_mask(shape, stride):
    """Regular grid sampling mask with given stride."""
    mask = np.zeros(shape, dtype=bool)
    mask[::stride, ::stride] = True
    return mask


def reconstruct_griddata(image, mask, method='cubic'):
    """
    Reconstruct a 2-D image from sparse samples using scipy griddata.

    Parameters
    ----------
    image : ndarray (n_x, n_y)  — full image (only masked pixels used)
    mask  : bool ndarray (n_x, n_y)
    method : 'linear', 'nearest', or 'cubic'
    """
    n_x, n_y = image.shape
    coords_all = np.stack(np.mgrid[0:n_x, 0:n_y], axis=-1).reshape(-1, 2)
    coords_sampled = coords_all[mask.ravel()]
    values_sampled = image[mask]

    recon_flat = griddata(coords_sampled, values_sampled,
                          coords_all, method=method)
    # Fill any NaN edge pixels with nearest
    nan_mask = np.isnan(recon_flat)
    if nan_mask.any():
        recon_flat[nan_mask] = griddata(
            coords_sampled, values_sampled,
            coords_all[nan_mask], method='nearest'
        )
    return recon_flat.reshape(n_x, n_y)


def reconstruct_rbf(image, mask, kernel='thin_plate_spline', smoothing=1e-3):
    """
    Reconstruct using Radial Basis Function interpolation.
    Better for smooth fields with moderate numbers of samples.
    """
    n_x, n_y = image.shape
    coords_all = np.stack(np.mgrid[0:n_x, 0:n_y], axis=-1).reshape(-1, 2)
    coords_sampled = coords_all[mask.ravel()]
    values_sampled = image[mask]

    rbf = RBFInterpolator(coords_sampled, values_sampled,
                          kernel=kernel, smoothing=smoothing)
    recon_flat = rbf(coords_all)
    return recon_flat.reshape(n_x, n_y)


def reconstruction_error(ground_truth, reconstruction):
    """Return per-pixel absolute error and RMSE."""
    error = reconstruction - ground_truth
    rmse = float(np.sqrt(np.mean(error ** 2)))
    return error, rmse


def spiral_mask(shape, n_turns=11, n_points=2600, random_state=None):
    """
    Generate a sparse **spiral scan** sampling pattern (Archimedean spiral).

    Spiral trajectories are used in fast SPM because they avoid the abrupt
    turnarounds of a raster and keep the tip moving smoothly.

    Parameters
    ----------
    shape : tuple (ny, nx)
    n_turns : float       number of spiral revolutions
    n_points : int        samples taken along the spiral (denser -> more pixels)

    Returns
    -------
    mask : bool ndarray (ny, nx)   sampled pixels
    path : tuple(xs, ys)           continuous spiral coordinates (for plotting)
    """
    ny, nx = shape
    cx, cy = (nx - 1) / 2.0, (ny - 1) / 2.0
    theta = np.linspace(0.0, 2 * np.pi * n_turns, int(n_points))
    rmax = min(cx, cy)
    r = rmax * theta / theta.max()
    xs = cx + r * np.cos(theta)
    ys = cy + r * np.sin(theta)
    xi = np.clip(np.round(xs).astype(int), 0, nx - 1)
    yi = np.clip(np.round(ys).astype(int), 0, ny - 1)
    mask = np.zeros(shape, dtype=bool)
    mask[yi, xi] = True
    return mask, (xs, ys)


def reconstruct_gp(image, mask, length_scale=5.0, noise_level=1e-2,
                   optimize=True, random_state=0):
    """
    Reconstruct a 2-D image from sparse samples with **Gaussian Process**
    regression. Unlike interpolation, a GP also returns a per-pixel
    **uncertainty** (predictive std) — high where samples are sparse.

    Returns
    -------
    mean : ndarray (ny, nx)   posterior mean (the reconstruction)
    std  : ndarray (ny, nx)   posterior standard deviation (uncertainty)
    """
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel

    ny, nx = image.shape
    coords = np.stack(np.mgrid[0:ny, 0:nx], axis=-1).reshape(-1, 2).astype(float)
    obs = mask.ravel()
    X_obs, y_obs = coords[obs], image.ravel()[obs]

    kernel = (ConstantKernel(1.0, (1e-2, 1e2))
              * RBF(length_scale, (1.0, 30.0))
              + WhiteKernel(noise_level, (1e-5, 1e-1)))
    gp = GaussianProcessRegressor(
        kernel=kernel, normalize_y=True, random_state=random_state,
        optimizer='fmin_l_bfgs_b' if optimize else None,
        n_restarts_optimizer=0)
    gp.fit(X_obs, y_obs)

    # predict in chunks to keep memory modest
    mean = np.empty(coords.shape[0]); std = np.empty(coords.shape[0])
    for i in range(0, coords.shape[0], 2048):
        sl = slice(i, i + 2048)
        mean[sl], std[sl] = gp.predict(coords[sl], return_std=True)
    return mean.reshape(ny, nx), std.reshape(ny, nx)
