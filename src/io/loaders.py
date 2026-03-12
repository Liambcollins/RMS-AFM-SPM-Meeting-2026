"""
Data loaders for SPM files.

Currently supports .npz (synthetic/processed) and basic image formats.
Stubs are provided for common proprietary formats — contributions welcome.
"""

import os
import numpy as np


def load_npz(path):
    """Load a .npz file and return a dict of arrays."""
    data = np.load(path, allow_pickle=False)
    return dict(data)


def load_image(path):
    """
    Load a grayscale image (PNG, TIFF, etc.) as a float32 array in [0, 1].
    Requires scikit-image.
    """
    from skimage import io as skio
    from skimage.color import rgb2gray
    img = skio.imread(path)
    if img.ndim == 3:
        img = rgb2gray(img)
    return img.astype(np.float32)


# ---------------------------------------------------------------------------
# Stubs for proprietary formats
# ---------------------------------------------------------------------------

def load_ibw(path):
    """Load an Igor Binary Wave (.ibw) file. Requires the `igor` package."""
    raise NotImplementedError(
        "IBW loading requires the `igor` package. "
        "Install with: pip install igor2"
    )


def load_sxm(path):
    """Load a Nanonis .sxm file. Requires the `nanonispy` package."""
    raise NotImplementedError(
        "SXM loading requires `nanonispy`. "
        "Install with: pip install nanonispy"
    )


def load_nid(path):
    """Load a JPK / Nanosurf .nid file. Requires `pySPM`."""
    raise NotImplementedError(
        "NID loading requires `pySPM`. "
        "Install with: pip install pySPM"
    )
