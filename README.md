# Machine Learning & AI in Scanning Probe Microscopy

**RMS AFM & SPM Meeting 2026 — Tutorial Session**
*Author: Liam Collins*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/00_setup_and_overview.ipynb)
[![View on nbviewer](https://img.shields.io/badge/view-nbviewer-orange)](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/tree/main/notebooks/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A practical, **big-picture tour** of how machine learning and AI support modern SPM workflows —
from regression and classification through denoising, clustering, smart/autonomous measurements,
and on to today's foundation models and agents. Every core example runs on **synthetic data**, so
no instrument files or downloads are required.

> This repo accompanies a ~25–30 min tutorial talk. It is meant to be browsed *or* run. See
> **[Two ways to use this repo](#two-ways-to-use-this-repo)** below.

---

## Two ways to use this repo

**💻 Run it** — on your own machine or in the browser, no install:

- **In your browser (zero setup):** click an *Open in Colab* badge in the table below. Colab clones
  the repo automatically (first cell) and runs everything on a free cloud machine.
- **On your computer:** clone the repo and create the environment ([Quick Start](#quick-start)).

**📱 View it** — just reading along on a phone or tablet? The notebooks are **pre-run with all figures
saved inside them**, so they render fully on GitHub and nbviewer with no execution:

- Tap the **nbviewer** link for any notebook below — clean, mobile-friendly, nothing to install.
- Or browse the `notebooks/` folder directly on GitHub.

---

## Tutorial modules

| # | Notebook | Topic | 💻 Run | 📱 View |
|---|----------|-------|:------:|:------:|
| 00 | `00_setup_and_overview` | Setup, motivation & a tour of SPM data | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/00_setup_and_overview.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/00_setup_and_overview.ipynb) |
| 01 | `01_pca_denoising` | PCA for denoising hyperspectral data | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/01_pca_denoising.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/01_pca_denoising.ipynb) |
| 02 | `02_clustering_phase_mapping` | Clustering for phase & domain mapping | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/02_clustering_phase_mapping.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/02_clustering_phase_mapping.ipynb) |
| 03 | `03_sparse_smart_measurements` | Sparse sampling & reconstruction | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/03_sparse_smart_measurements.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/03_sparse_smart_measurements.ipynb) |
| 04 | `04_autonomous_spm` | Adaptive / autonomous measurement loops | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/04_autonomous_spm.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/04_autonomous_spm.ipynb) |
| 05 | `05_regression_calibration` | Regression: calibration & property prediction | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/05_regression_calibration.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/05_regression_calibration.ipynb) |
| 06 | `06_classification_scan_qc` | Classification: automated scan QC | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/06_classification_scan_qc.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/06_classification_scan_qc.ipynb) |
| 07 | `07_neural_networks` | Neural networks & deep learning | [Colab](https://colab.research.google.com/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/07_neural_networks.ipynb) | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/07_neural_networks.ipynb) |

### Real-data showcase

| Notebook | Topic | 📱 View |
|----------|-------|:------:|
| `annexin_hsafm` | Annexin V assembly dynamics on lipid bilayers — **real High-Speed AFM** data, with PCA denoising, clustering & dynamics mapping | [nbviewer](https://nbviewer.org/github/Liambcollins/RMS-AFM-SPM-Meeting-2026/blob/main/notebooks/annexin_hsafm.ipynb) |

*This notebook downloads a published HS-AFM dataset, so run it locally or on Colab rather than relying on the browser preview.*

### Optional / advanced modules (`notebooks/optional/`)

| # | Notebook | Topic |
|---|----------|-------|
| 08 | `08_manifold_learning` | UMAP / t-SNE for hyperspectral data |
| 09 | `09_segmentation` | Image segmentation (Otsu, watershed, SLIC) |
| 10 | `10_physics_informed_ml` | Physics-informed ML for spectroscopy |

*Optional modules are illustrative scaffolds — run them yourself; they are not pre-rendered.*

---

## Suggested order for the talk

The notebooks build from the most familiar ideas to the frontier:

1. **Supervised basics** — regression (05) and classification (06): predict a number, predict a label.
2. **Neural networks** (07): when and why to go deeper.
3. **Unsupervised tools** — PCA denoising (01) and clustering (02): find structure without labels.
4. **Measure smarter** — sparse sampling (03) and autonomous SPM (04).
5. **Real data** — the Annexin V HS-AFM case study.

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Liambcollins/RMS-AFM-SPM-Meeting-2026.git
cd RMS-AFM-SPM-Meeting-2026
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
├── notebooks/          # Tutorial notebooks (start here) — pre-run with figures
│   ├── optional/       # Advanced / optional modules
│   └── annexin_exports/# Cached HS-AFM exports used by the real-data notebook
├── src/                # Reusable helper modules
│   ├── synthetic/      # Synthetic data generators (images, spectra, F-D curves, QC features)
│   ├── ml/             # ML tools (PCA, clustering, reconstruction, active learning)
│   ├── viz/            # Plotting helpers
│   ├── io/             # Data loaders
│   └── utils/          # Miscellaneous utilities
├── figures/            # Figures used in the slides (generated from the notebooks)
├── data/               # Data storage (synthetic generated at runtime)
├── docs/               # Documentation and landing page
└── exercises/          # Workshop exercise prompts
```

---

## Requirements

- Python 3.10+
- numpy, scipy, matplotlib, scikit-learn, scikit-image, pandas
- JupyterLab or Notebook

See `environment.yml` or `requirements.txt` for the full list. The supervised-learning notebooks
(05–07) use scikit-learn only; deep-learning frameworks (e.g. PyTorch) are discussed but not required.

---

## License

MIT License — see `LICENSE` for details.

---

> **Note:** This repository is under active development. If you spot a bug, an unclear section, or
> have a suggestion, please open an issue — contributions and feedback are very welcome.
