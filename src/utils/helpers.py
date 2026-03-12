"""
Miscellaneous utilities.
"""

import sys
import os
import numpy as np


def repo_root():
    """Return the repository root directory (two levels up from this file)."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def add_src_to_path():
    """
    Add the repo's src/ directory to sys.path so notebooks can import helpers.
    Call this at the top of each notebook.
    """
    root = repo_root()
    src = os.path.join(root, 'src')
    if src not in sys.path:
        sys.path.insert(0, src)
    return src


def normalise(arr, vmin=None, vmax=None):
    """Normalise array to [0, 1] using given or data min/max."""
    a = arr.astype(float)
    lo = vmin if vmin is not None else a.min()
    hi = vmax if vmax is not None else a.max()
    return np.clip((a - lo) / (hi - lo + 1e-12), 0, 1)


def snr_db(signal, noisy):
    """Compute signal-to-noise ratio in dB between clean and noisy arrays."""
    noise = noisy - signal
    power_signal = np.mean(signal ** 2)
    power_noise = np.mean(noise ** 2)
    if power_noise == 0:
        return np.inf
    return 10 * np.log10(power_signal / power_noise)


def cache_npz(path, generator_fn, *args, force=False, **kwargs):
    """
    Load a .npz cache file if it exists, otherwise call generator_fn and save.

    Returns the dict of arrays from the npz.
    """
    if not force and os.path.exists(path):
        data = np.load(path)
        return dict(data)
    result = generator_fn(*args, **kwargs)
    if isinstance(result, dict):
        np.savez(path, **result)
        return result
    raise ValueError("generator_fn must return a dict of arrays")
