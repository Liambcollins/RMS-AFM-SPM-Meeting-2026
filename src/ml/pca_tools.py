"""
PCA-based tools for hyperspectral SPM data.
"""

import numpy as np
from sklearn.decomposition import PCA


def flatten_cube(cube):
    """
    Reshape a (n_x, n_y, n_freq) cube to (n_pixels, n_freq).
    Returns the flat array and the original spatial shape.
    """
    n_x, n_y, n_freq = cube.shape
    return cube.reshape(n_x * n_y, n_freq), (n_x, n_y)


def pca_decompose(cube, n_components=None, return_model=False):
    """
    Decompose a (n_x, n_y, n_freq) hyperspectral cube with PCA.

    Returns
    -------
    scores : ndarray, shape (n_pixels, n_components)
        PCA scores (projections).
    components : ndarray, shape (n_components, n_freq)
        PCA components (eigenvectors in frequency space).
    explained_variance_ratio : ndarray
    model : PCA  (only if return_model=True)
    """
    flat, spatial_shape = flatten_cube(cube)
    n_comp = n_components or min(flat.shape)
    model = PCA(n_components=n_comp, svd_solver='full', random_state=0)
    scores = model.fit_transform(flat)
    if return_model:
        return scores, model.components_, model.explained_variance_ratio_, model
    return scores, model.components_, model.explained_variance_ratio_


def pca_reconstruct(cube, n_components):
    """
    Denoise a hyperspectral cube by keeping only the first n_components PCs.

    Returns
    -------
    denoised : ndarray, same shape as cube
    """
    flat, spatial_shape = flatten_cube(cube)
    model = PCA(n_components=n_components, svd_solver='full', random_state=0)
    scores = model.fit_transform(flat)
    denoised_flat = model.inverse_transform(scores)
    return denoised_flat.reshape(cube.shape)


def component_maps(scores, spatial_shape, n_show=None):
    """
    Reshape PCA scores back to spatial maps.

    Returns ndarray, shape (n_components, n_x, n_y).
    """
    n_pix, n_comp = scores.shape
    n_show = n_show or n_comp
    maps = scores[:, :n_show].reshape(spatial_shape[0], spatial_shape[1], n_show)
    return np.moveaxis(maps, -1, 0)  # (n_show, n_x, n_y)
