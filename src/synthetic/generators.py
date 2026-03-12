"""
Synthetic data generators for SPM-like datasets.

All functions return numpy arrays and accept a random_state parameter
for reproducibility.
"""

import numpy as np
from scipy.ndimage import gaussian_filter


def make_domain_image(size=64, n_domains=4, smooth_sigma=3.0, noise_level=0.1,
                      random_state=42):
    """
    Generate a synthetic SPM height/phase image with domain structure.

    Returns a (size, size) array with values roughly in [0, 1],
    representing distinct spatial domains (e.g. ferroelectric phases,
    polymer microstructure, grain structure).

    Parameters
    ----------
    size : int
        Image side length in pixels.
    n_domains : int
        Number of distinct phase domains.
    smooth_sigma : float
        Gaussian smoothing applied to the domain map.
    noise_level : float
        Std of Gaussian noise added to the final image.
    random_state : int or None
        Random seed.
    """
    rng = np.random.default_rng(random_state)

    # Voronoi-like domain map: assign each pixel to nearest random seed
    seeds = rng.integers(0, size, size=(n_domains, 2))
    coords = np.stack(np.mgrid[0:size, 0:size], axis=-1)  # (size, size, 2)
    dists = np.linalg.norm(
        coords[:, :, None, :] - seeds[None, None, :, :], axis=-1
    )  # (size, size, n_domains)
    domain_map = dists.argmin(axis=-1).astype(float)

    # Assign each domain a distinct value
    values = np.linspace(0, 1, n_domains)
    rng.shuffle(values)
    image = values[domain_map.astype(int)]

    # Smooth edges slightly
    image = gaussian_filter(image, sigma=smooth_sigma * 0.3)

    # Add noise
    image += rng.normal(0, noise_level, image.shape)
    return image.astype(np.float32)


def make_grain_image(size=64, n_grains=12, noise_level=0.15, random_state=42):
    """
    Generate a synthetic polycrystalline grain image.

    Each grain has a slightly different background value plus
    orientation-like texture, mimicking AFM phase or friction images.
    """
    rng = np.random.default_rng(random_state)

    seeds = rng.integers(0, size, size=(n_grains, 2))
    coords = np.stack(np.mgrid[0:size, 0:size], axis=-1)
    dists = np.linalg.norm(
        coords[:, :, None, :] - seeds[None, None, :, :], axis=-1
    )
    grain_map = dists.argmin(axis=-1)

    grain_values = rng.uniform(0.2, 0.9, n_grains)
    image = grain_values[grain_map]

    # Add grain-boundary darkening
    grain_boundary = np.zeros((size, size), dtype=float)
    for shift in [(1, 0), (0, 1)]:
        shifted = np.roll(grain_map, shift, axis=(0, 1))
        grain_boundary += (grain_map != shifted).astype(float)
    image -= 0.3 * np.clip(grain_boundary, 0, 1)

    image += rng.normal(0, noise_level, image.shape)
    image = np.clip(image, 0, 1)
    return image.astype(np.float32)


def make_hyperspectral_spm(n_x=32, n_y=32, n_freq=64, n_components=3,
                            noise_level=0.3, random_state=42):
    """
    Generate synthetic hyperspectral SPM data (e.g. KPFM, EFM, SSPFM).

    Returns
    -------
    cube : ndarray, shape (n_x, n_y, n_freq)
        Hyperspectral data cube. Each pixel contains a spectrum.
    spectra : ndarray, shape (n_components, n_freq)
        The ground-truth component spectra.
    maps : ndarray, shape (n_components, n_x, n_y)
        The ground-truth spatial abundance maps.
    freq_axis : ndarray, shape (n_freq,)
        Frequency axis (arbitrary units, 0–1).
    """
    rng = np.random.default_rng(random_state)
    freq_axis = np.linspace(0, 1, n_freq)

    # Build a few latent spectra (Gaussian peaks at different positions)
    spectra = np.zeros((n_components, n_freq))
    centers = np.linspace(0.15, 0.85, n_components)
    widths = rng.uniform(0.05, 0.12, n_components)
    for i in range(n_components):
        spectra[i] = np.exp(-0.5 * ((freq_axis - centers[i]) / widths[i]) ** 2)
        spectra[i] /= spectra[i].max()

    # Build spatial abundance maps via domain structure
    maps = np.zeros((n_components, n_x, n_y))
    domain_img = make_domain_image(
        size=max(n_x, n_y), n_domains=n_components,
        smooth_sigma=3.0, noise_level=0.0, random_state=random_state
    )[:n_x, :n_y]

    # Assign each pixel to one dominant component
    edges = np.linspace(0, 1, n_components + 1)
    for i in range(n_components):
        mask = (domain_img >= edges[i]) & (domain_img < edges[i + 1])
        maps[i][mask] = rng.uniform(0.7, 1.0, mask.sum())
        # Small cross-contributions
        for j in range(n_components):
            if j != i:
                maps[j][mask] += rng.uniform(0.0, 0.15, mask.sum())

    # Normalise maps so they sum to ~1 per pixel
    maps_sum = maps.sum(axis=0, keepdims=True) + 1e-8
    maps /= maps_sum

    # Build the data cube
    cube = np.einsum('cxy,cf->xyf', maps, spectra)

    # Add noise
    cube += rng.normal(0, noise_level * cube.max(), cube.shape)

    return cube.astype(np.float32), spectra.astype(np.float32), \
           maps.astype(np.float32), freq_axis.astype(np.float32)


def make_sparse_target_image(size=64, feature_type='mixed', random_state=42):
    """
    Generate a smooth synthetic image suitable for sparse-sampling demos.

    Parameters
    ----------
    feature_type : str
        'smooth'  — broad smooth bumps (easy to reconstruct)
        'edges'   — domain-like regions with sharp boundaries
        'mixed'   — both smooth and edge features
    """
    rng = np.random.default_rng(random_state)
    coords = np.stack(np.mgrid[0:size, 0:size], axis=-1) / size

    image = np.zeros((size, size))

    if feature_type in ('smooth', 'mixed'):
        # Broad Gaussian bumps
        n_bumps = rng.integers(3, 8)
        for _ in range(n_bumps):
            cx, cy = rng.uniform(0.1, 0.9, 2)
            sigma = rng.uniform(0.08, 0.25)
            amp = rng.uniform(0.3, 1.0)
            r2 = ((coords[..., 0] - cx) ** 2 + (coords[..., 1] - cy) ** 2)
            image += amp * np.exp(-r2 / (2 * sigma ** 2))

    if feature_type in ('edges', 'mixed'):
        domain = make_domain_image(size=size, n_domains=3, smooth_sigma=2.0,
                                   noise_level=0.0, random_state=random_state + 1)
        image += domain

    # Normalise to [0, 1]
    image -= image.min()
    image /= image.max() + 1e-8
    return image.astype(np.float32)


def make_adaptive_target(size=32, random_state=42):
    """
    Generate a ground-truth map for the autonomous measurement demo.

    Returns a (size, size) float array with localised features
    (sharp peaks / edges) that a smart sampler should discover.
    """
    rng = np.random.default_rng(random_state)
    image = np.zeros((size, size))
    coords = np.stack(np.mgrid[0:size, 0:size], axis=-1).astype(float) / size

    # A few narrow peaks
    for _ in range(rng.integers(2, 5)):
        cx, cy = rng.uniform(0.1, 0.9, 2)
        sigma = rng.uniform(0.04, 0.12)
        r2 = ((coords[..., 0] - cx) ** 2 + (coords[..., 1] - cy) ** 2)
        image += rng.uniform(0.4, 1.0) * np.exp(-r2 / (2 * sigma ** 2))

    # Smooth background
    bg = make_domain_image(size=size, n_domains=2, smooth_sigma=4.0,
                           noise_level=0.0, random_state=random_state + 7)
    image += 0.2 * bg

    image -= image.min()
    image /= image.max() + 1e-8
    return image.astype(np.float32)
