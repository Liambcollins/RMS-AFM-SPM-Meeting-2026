"""
Clustering tools for SPM phase and domain mapping.
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler


def kmeans_cluster(features, n_clusters, random_state=42, n_init=10):
    """
    Apply KMeans to a flat (n_samples, n_features) array.

    Returns
    -------
    labels : ndarray, shape (n_samples,)
    model : fitted KMeans
    """
    model = KMeans(n_clusters=n_clusters, random_state=random_state,
                   n_init=n_init)
    labels = model.fit_predict(features)
    return labels, model


def gmm_cluster(features, n_components, random_state=42):
    """
    Apply Gaussian Mixture Model clustering.

    Returns
    -------
    labels : ndarray, shape (n_samples,)
    probs  : ndarray, shape (n_samples, n_components)  — soft assignments
    model  : fitted GaussianMixture
    """
    model = GaussianMixture(n_components=n_components,
                            covariance_type='full',
                            random_state=random_state,
                            n_init=3)
    model.fit(features)
    labels = model.predict(features)
    probs = model.predict_proba(features)
    return labels, probs, model


def cluster_cube(cube, n_clusters, method='kmeans', use_pca=True,
                 n_pca=10, random_state=42):
    """
    Cluster a (n_x, n_y, n_feat) hyperspectral cube.

    Returns
    -------
    label_map : ndarray, shape (n_x, n_y)
    """
    n_x, n_y, n_feat = cube.shape
    flat = cube.reshape(n_x * n_y, n_feat)

    # Optionally reduce dimensionality first
    if use_pca and n_feat > n_pca:
        from sklearn.decomposition import PCA
        pca = PCA(n_components=min(n_pca, flat.shape[1]), random_state=random_state)
        flat = pca.fit_transform(flat)

    # Standardise
    scaler = StandardScaler()
    flat_scaled = scaler.fit_transform(flat)

    if method == 'kmeans':
        labels, _ = kmeans_cluster(flat_scaled, n_clusters,
                                   random_state=random_state)
    elif method == 'gmm':
        labels, _, _ = gmm_cluster(flat_scaled, n_clusters,
                                   random_state=random_state)
    else:
        raise ValueError(f"Unknown method: {method!r}")

    return labels.reshape(n_x, n_y)


def relabel_by_size(label_map):
    """Re-index cluster labels so label 0 is the largest cluster."""
    labels_flat = label_map.ravel()
    unique, counts = np.unique(labels_flat, return_counts=True)
    order = unique[np.argsort(-counts)]
    mapping = {old: new for new, old in enumerate(order)}
    return np.vectorize(mapping.get)(label_map)
