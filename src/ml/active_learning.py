"""
Simple adaptive / active measurement utilities for the autonomous SPM demo.

Deliberately lightweight — no GP library required. We use a simple
RBF-smoothed uncertainty model based on distance to measured points.
"""

import numpy as np
from scipy.interpolate import RBFInterpolator
from scipy.ndimage import gaussian_filter


def distance_uncertainty(mask, shape, decay=5.0):
    """
    Compute a simple distance-based uncertainty map.

    Pixels far from any measurement have high uncertainty.
    `decay` controls the length scale (in pixels).
    """
    # Build distance transform from measured pixels
    from scipy.ndimage import distance_transform_edt
    not_measured = ~mask
    dist = distance_transform_edt(not_measured)
    uncertainty = 1.0 - np.exp(-dist / decay)
    return uncertainty.astype(np.float32)


def gradient_score(model_estimate):
    """
    Score pixels by local gradient magnitude of the current model estimate.
    Regions with high gradient are informative — sample them next.
    """
    gy, gx = np.gradient(model_estimate)
    grad_mag = np.sqrt(gx ** 2 + gy ** 2)
    # Smooth to avoid chasing noise
    grad_mag = gaussian_filter(grad_mag, sigma=1.5)
    return grad_mag.astype(np.float32)


def acquisition_function(uncertainty, gradient=None, alpha=0.7):
    """
    Combine uncertainty and gradient scores into an acquisition map.

    Higher values indicate more informative measurement locations.

    Parameters
    ----------
    alpha : float
        Weight on uncertainty vs gradient (1.0 = pure uncertainty).
    """
    score = alpha * uncertainty
    if gradient is not None:
        g = gradient / (gradient.max() + 1e-8)
        score += (1.0 - alpha) * g
    return score


def select_next_point(acquisition, mask, n_candidates=5, random_state=None):
    """
    Select the next measurement point from the acquisition map.

    Excludes already-measured pixels. Returns (row, col).
    """
    rng = np.random.default_rng(random_state)
    acq = acquisition.copy()
    acq[mask] = -np.inf  # exclude measured pixels

    # Top-k candidates with small random jitter to avoid always repeating same
    flat = acq.ravel()
    top_k = np.argsort(flat)[-n_candidates:]
    chosen_flat = rng.choice(top_k)
    row, col = np.unravel_index(chosen_flat, acquisition.shape)
    return int(row), int(col)


def rbf_estimate(mask, values_at_mask, shape, smoothing=0.1):
    """
    Build a smooth model estimate over the full grid from sparse measurements.

    Parameters
    ----------
    mask   : bool array (n_x, n_y)
    values : 1-D array of measured values
    shape  : (n_x, n_y)

    Returns
    -------
    estimate : ndarray (n_x, n_y)
    """
    n_x, n_y = shape
    coords_all = np.stack(np.mgrid[0:n_x, 0:n_y], axis=-1).reshape(-1, 2)
    coords_obs = coords_all[mask.ravel()]

    if len(coords_obs) < 4:
        return np.zeros(shape, dtype=np.float32)

    rbf = RBFInterpolator(coords_obs, values_at_mask,
                          kernel='thin_plate_spline', smoothing=smoothing)
    est = rbf(coords_all).reshape(n_x, n_y)
    return est.astype(np.float32)
