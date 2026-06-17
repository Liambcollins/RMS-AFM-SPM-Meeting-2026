# Datasets

## Synthetic data (default)

All tutorial notebooks generate synthetic data at runtime using functions in `src/synthetic/generators.py`. No downloads required.

| Generator function | Description | Used in |
|--------------------|-------------|---------|
| `make_domain_image` | Voronoi-like domain/phase image | 00, 02 |
| `make_grain_image` | Polycrystalline grain image | 00 |
| `make_hyperspectral_spm` | Hyperspectral cube with latent spectral components | 01, 02 |
| `make_sparse_target_image` | Smooth image with bumps and edges for sparse sampling | 03 |
| `make_adaptive_target` | Sharp-feature image for adaptive measurement | 04 |
| `make_fd_curve` | Synthetic force–distance curve (Hertzian contact + adhesion + noise) | 05 |
| `make_modulus_dataset` | Tabular features → Young's modulus regression target | 05 |
| `make_scan_quality_dataset` | Tabular scan-quality features → good/bad labels | 06, 07 |

Generated datasets can optionally be cached to `data/synthetic/` as `.npz` files using `src/utils/helpers.cache_npz`.

## Real experimental data

Real SPM files are **not** included in this repository. To load real data:

- **IBW** (Igor Pro): install `igor2` — `pip install igor2`
- **SXM** (Nanonis): install `nanonispy` — `pip install nanonispy`
- **NID** (JPK/Nanosurf): install `pySPM` — `pip install pySPM`

See `src/io/loaders.py` for stub loaders. Contributions of real-data loaders are welcome.

## Data directory layout

```
data/
├── raw/          ← place real experimental files here (not tracked by git)
├── synthetic/    ← cached synthetic datasets (auto-generated)
└── processed/    ← intermediate outputs (e.g. preprocessed cubes)
```
