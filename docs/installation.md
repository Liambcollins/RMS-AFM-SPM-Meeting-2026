# Installation Guide

## Prerequisites

- Python 3.10 or later
- conda (recommended) or pip

## Option 1: conda (recommended)

```bash
conda env create -f environment.yml
conda activate spm-ml-tutorial
```

## Option 2: pip

```bash
pip install -r requirements.txt
```

## Launch JupyterLab

```bash
jupyter lab
```

Then navigate to the `notebooks/` folder and open any `.ipynb` file.

## Verify the installation

Open `notebooks/00_setup_and_overview.ipynb` and run the first two cells. You should see version info and "All imports OK".

## Troubleshooting

See [troubleshooting.md](troubleshooting.md) if you run into issues.

## Optional dependencies

- `umap-learn` — required for notebook 05 (manifold learning):
  ```bash
  pip install umap-learn
  ```
- `scikit-image` — required for notebook 06 (segmentation); included in the default environment.
