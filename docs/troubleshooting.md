# Troubleshooting

## "ModuleNotFoundError: No module named 'src'"

Each notebook adds the `src/` directory to `sys.path` with:

```python
import sys, os
sys.path.insert(0, os.path.join('..', 'src'))
```

This assumes you launch JupyterLab from the **repository root**. If you launch from elsewhere, adjust the path accordingly, e.g.:

```python
sys.path.insert(0, '/absolute/path/to/repo/src')
```

## "ModuleNotFoundError: No module named 'synthetic'"

Make sure you ran the `sys.path.insert` cell before any import cell. Restart the kernel and run all cells from the top.

## "ImportError: cannot import name 'plot_scree' from 'viz.plotting'"

The `src/viz/plotting.py` file may be out of date. Pull the latest version from the repository.

## Kernel crashes on large datasets

Notebook 01 uses a 32×32×64 cube by default — very small. If you scale up (e.g. 128×128×256), memory use increases significantly. Reduce `n_x`, `n_y`, or `n_freq` in `make_hyperspectral_spm` if you see memory issues.

## Plots not displaying

If using JupyterLab and plots don't appear, try adding `%matplotlib inline` at the top of your setup cell.

## conda environment not appearing in Jupyter

```bash
conda activate spm-ml-tutorial
conda install -c conda-forge ipykernel
python -m ipykernel install --user --name spm-ml-tutorial
```

Then restart JupyterLab and select the `spm-ml-tutorial` kernel.

## Reporting issues

Please open an issue on GitHub — all reports are appreciated.
