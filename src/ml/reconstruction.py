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
