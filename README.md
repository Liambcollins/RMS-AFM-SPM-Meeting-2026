# Machine Learning in Scanning Probe Microscopy

**RMS AFM & SPM Meeting 2026 Tutorial**
*Author: Liam Collins*

This repository contains notebooks, demos, and helper code for the tutorial on **Machine Learning in Scanning Probe Microscopy** at the RMS AFM & SPM Meeting 2026.

The goal is to provide practical, hands-on examples showing how machine learning can support modern SPM workflows — from denoising and clustering through to smart measurements and autonomous experimentation. All examples run on synthetic data, so no proprietary instrument files are needed.

> **Note:** This repository is under active development and probably always will be. Some examples may be incomplete, rough around the edges, or contain mistakes. Apologies in advance for any issues — please feel free to report bugs, unclear sections, or suggestions via the Issues tab.

---

## Tutorial Modules

| # | Notebook | Topic |
|---|----------|-------|
| 00 | `00_setup_and_overview.ipynb` | Setup, motivation, and tour |
| 01 | `01_pca_denoising.ipynb` | PCA for denoising hyperspectral data |
| 02 | `02_clustering_phase_mapping.ipynb` | Clustering for phase and domain mapping |
| 03 | `03_sparse_smart_measurements.ipynb` | Sparse sampling and reconstruction |
| 04 | `04_autonomous_spm.ipynb` | Adaptive / autonomous measurement loops |

**Optional / advanced modules** (in `notebooks/optional/`):

| # | Notebook | Topic |
|---|----------|-------|
| 05 | `05_manifold_learning.ipynb` | UMAP / t-SNE for hyperspectral data |
| 06 | `06_segmentation.ipynb` | Image segmentation |
| 07 | `07_physics_informed_ml.ipynb` | Physics-informed ML for spectroscopy |

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/liamcollins/rms-spm-ml-tutorial-2026.git
cd rms-spm-ml-tutorial-2026
```

### 2. Create the environment

**With conda (recommended):**
```bash
conda env create -f environment.yml
conda activate spm-ml-tutorial
```

**With pip:**
```bash
pip install -r requirements.txt
```

### 3. Launch JupyterLab
```bash
jupyter lab
```

Then open any notebook in the `notebooks/` folder.

---

## Repository Structure

```
├── notebooks/          # Tutorial notebooks (start here)
├── src/                # Reusable helper modules
│   ├── synthetic/      # Synthetic data generators
│   ├── ml/             # ML tools (PCA, clustering, etc.)
│   ├── viz/            # Plotting helpers
│   ├── io/             # Data loaders
│   └── utils/          # Miscellaneous utilities
├── data/               # Data storage (synthetic generated at runtime)
├── figures/            # Saved figures
├── docs/               # Documentation and landing page
└── exercises/          # Workshop exercise prompts
```

---

## Requirements

- Python 3.10+
- numpy, scipy, matplotlib, scikit-learn, scikit-image
- JupyterLab or Notebook

See `environment.yml` or `requirements.txt` for the full list.

---

## License

MIT License — see `LICENSE` for details.
