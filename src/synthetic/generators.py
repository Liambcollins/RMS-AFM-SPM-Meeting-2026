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


# ---------------------------------------------------------------------------
# Supervised-learning datasets (regression & classification)
# ---------------------------------------------------------------------------

def make_fd_curve(z_nm=None, k_cantilever=0.4, invols_nm_per_v=55.0,
                  E_modulus_kpa=120.0, adhesion_nn=4.0, tip_radius_nm=20.0,
                  contact_point_nm=0.0, noise_pn=120.0, random_state=42):
    """
    Generate a synthetic AFM force-distance (F-D) curve (approach segment).

    Physics: free region (no force) before contact, then a Hertzian contact
    regime F = (4/3) E* sqrt(R) delta^(3/2) once the tip indents the surface,
    plus an attractive adhesion offset and detector noise.

    Returns
    -------
    z_nm : ndarray  (piezo z position, nm)
    force_nn : ndarray  (measured force, nN)
    meta : dict  (ground-truth parameters)
    """
    rng = np.random.default_rng(random_state)
    if z_nm is None:
        z_nm = np.linspace(-60.0, 40.0, 400)  # negative = approaching, positive = indenting

    E_pa = E_modulus_kpa * 1e3
    E_star = E_pa / (1 - 0.5 ** 2)          # Poisson ratio 0.5 (soft matter)
    R = tip_radius_nm * 1e-9

    delta = np.clip(z_nm - contact_point_nm, 0, None) * 1e-9  # indentation (m)
    F_contact = (4.0 / 3.0) * E_star * np.sqrt(R) * delta ** 1.5  # N
    force_nn = F_contact * 1e9                                    # nN
    force_nn += rng.normal(0, noise_pn * 1e-3, force_nn.shape)     # detector noise (nN)

    meta = dict(k_cantilever=k_cantilever, invols_nm_per_v=invols_nm_per_v,
                E_modulus_kpa=E_modulus_kpa, adhesion_nn=adhesion_nn,
                tip_radius_nm=tip_radius_nm, contact_point_nm=contact_point_nm)
    return z_nm.astype(np.float32), force_nn.astype(np.float32), meta


def make_modulus_dataset(n_samples=400, random_state=42):
    """
    Tabular regression dataset: predict sample Young's modulus from features
    extracted from force-distance curves.

    Features (per curve): contact_stiffness, adhesion, indentation_depth,
    contact_slope, noise_rms. Target: Young's modulus (kPa).

    Returns
    -------
    X : ndarray (n_samples, 5)
    y : ndarray (n_samples,)   modulus in kPa
    feature_names : list[str]
    """
    rng = np.random.default_rng(random_state)
    E = rng.uniform(20, 400, n_samples)                       # true modulus (kPa)
    contact_stiffness = 0.08 * E + rng.normal(0, 1.5, n_samples)      # ~ linear in E
    indentation = 220.0 / np.sqrt(E) + rng.normal(0, 3.0, n_samples)  # softer -> deeper
    contact_slope = 0.05 * E + rng.normal(0, 1.0, n_samples)
    adhesion = rng.uniform(1, 8, n_samples) + 0.004 * E              # weak coupling
    noise_rms = rng.uniform(0.05, 0.25, n_samples)
    X = np.column_stack([contact_stiffness, adhesion, indentation,
                         contact_slope, noise_rms]).astype(np.float32)
    feature_names = ['contact_stiffness', 'adhesion', 'indentation_depth',
                     'contact_slope', 'noise_rms']
    return X, E.astype(np.float32), feature_names


def make_scan_quality_dataset(n_samples=600, random_state=42):
    """
    Tabular classification dataset: label an SPM scan as 'good' (0) or
    'bad' (1) from simple image-quality features.

    Bad scans (tip crashes, streaking, drift, contamination) have higher
    line-to-line noise and drift and lower feature contrast.

    Returns
    -------
    X : ndarray (n_samples, 2)   [line_noise, feature_contrast]  (for 2-D demos)
    X_full : ndarray (n_samples, 4)  adds [drift, fft_sharpness]
    y : ndarray (n_samples,)  0 = good, 1 = bad
    feature_names : list[str]
    """
    rng = np.random.default_rng(random_state)
    n_bad = n_samples // 2
    n_good = n_samples - n_bad

    # good scans: low line noise, high contrast
    good_noise = rng.normal(0.18, 0.05, n_good)
    good_contrast = rng.normal(0.75, 0.10, n_good)
    good_drift = rng.normal(0.10, 0.04, n_good)
    good_fft = rng.normal(0.70, 0.10, n_good)

    # bad scans: high line noise, low contrast (with overlap -> nonlinear-ish)
    bad_noise = rng.normal(0.45, 0.12, n_bad)
    bad_contrast = rng.normal(0.45, 0.15, n_bad)
    bad_drift = rng.normal(0.35, 0.12, n_bad)
    bad_fft = rng.normal(0.40, 0.15, n_bad)

    noise = np.concatenate([good_noise, bad_noise])
    contrast = np.concatenate([good_contrast, bad_contrast])
    drift = np.concatenate([good_drift, bad_drift])
    fft = np.concatenate([good_fft, bad_fft])
    y = np.concatenate([np.zeros(n_good), np.ones(n_bad)]).astype(int)

    X2 = np.column_stack([noise, contrast]).astype(np.float32)
    X4 = np.column_stack([noise, contrast, drift, fft]).astype(np.float32)
    names = ['line_noise', 'feature_contrast', 'drift', 'fft_sharpness']
    # shuffle
    order = rng.permutation(n_samples)
    return X2[order], X4[order], y[order], names


def make_force_volume(size=44, n_z=100, z_min_nm=-15.0, z_max_nm=50.0,
                      moduli_kpa=(35.0, 95.0, 190.0), tip_radius_nm=20.0,
                      e_jitter=0.10, noise_nn=0.03, random_state=42):
    """
    Synthetic AFM force-volume dataset for clustering demos.

    Topography shows only **two** height levels, but the mechanical response
    (Hertzian force-vs-indentation curves) splits into **three** clusters — a
    stiff phase is hidden inside one of the height regions and is invisible in
    topography. Clustering the force curves recovers all three phases.

    Returns
    -------
    height : ndarray (size, size)         topography (2 visible levels)
    force  : ndarray (size, size, n_z)    approach force curves (nN)
    z_nm   : ndarray (n_z,)               common z / indentation axis (nm), contact at 0
    true_label : ndarray (size, size)     ground-truth mechanical phase (0,1,2)
    """
    rng = np.random.default_rng(random_state)

    # Three Voronoi regions -> ground-truth mechanical phases
    seeds = rng.integers(0, size, size=(3, 2))
    coords = np.stack(np.mgrid[0:size, 0:size], axis=-1)
    dists = np.linalg.norm(coords[:, :, None, :] - seeds[None, None, :, :], axis=-1)
    true_label = dists.argmin(axis=-1).astype(int)            # 0,1,2

    # Topography: phases 0 and 1 share a height (hidden boundary); phase 2 is raised
    height = np.where(true_label == 2, 4.0, 1.0).astype(float)
    height = gaussian_filter(height, sigma=1.0)
    height += rng.normal(0, 0.06, height.shape)

    # Common z axis; contact at z = 0, free (F~0) before contact
    z_nm = np.linspace(z_min_nm, z_max_nm, n_z)
    R = tip_radius_nm * 1e-9
    delta = np.clip(z_nm, 0, None) * 1e-9                      # indentation (m)
    delta15 = delta ** 1.5

    force = np.zeros((size, size, n_z), dtype=np.float32)
    moduli_kpa = np.asarray(moduli_kpa, float)
    for p in range(3):
        mask = true_label == p
        n = int(mask.sum())
        E = moduli_kpa[p] * 1e3 * (1 + rng.normal(0, e_jitter, n))   # per-pixel modulus (Pa)
        E_star = E / (1 - 0.5 ** 2)                                  # Poisson 0.5
        # F (nN) = (4/3) E* sqrt(R) delta^1.5  * 1e9
        base = (4.0 / 3.0) * E_star[:, None] * np.sqrt(R) * delta15[None, :] * 1e9
        base += rng.normal(0, noise_nn, base.shape)
        force[mask] = base.astype(np.float32)

    return (height.astype(np.float32), force, z_nm.astype(np.float32),
            true_label.astype(int))
