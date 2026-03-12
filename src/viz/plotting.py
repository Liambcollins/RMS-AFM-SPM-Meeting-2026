"""
Plotting helpers for the SPM ML tutorial.

All functions return matplotlib Figure objects (or axes) so callers
can save or further customise them.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import Normalize


# ---------------------------------------------------------------------------
# Style helpers
# ---------------------------------------------------------------------------

def set_style(context='notebook'):
    """Apply a clean, tutorial-friendly matplotlib style."""
    plt.rcParams.update({
        'figure.facecolor': 'white',
        'axes.facecolor':   'white',
        'axes.grid':        False,
        'font.size':        11,
        'axes.titlesize':   12,
        'axes.labelsize':   11,
        'xtick.labelsize':  9,
        'ytick.labelsize':  9,
        'image.cmap':       'viridis',
        'figure.dpi':       100,
    })


# ---------------------------------------------------------------------------
# SPM image helpers
# ---------------------------------------------------------------------------

def show_image(image, title='', cmap='viridis', colorbar=True,
               ax=None, fig=None, **kwargs):
    """Display a single 2-D SPM image with optional colorbar."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))
    im = ax.imshow(image, cmap=cmap, origin='lower', **kwargs)
    ax.set_title(title)
    ax.set_xlabel('x (px)')
    ax.set_ylabel('y (px)')
    if colorbar:
        if fig is None:
            fig = ax.get_figure()
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    return ax


def compare_images(images, titles=None, cmap='viridis', figsize=None,
                   suptitle='', colorbar=True):
    """
    Display multiple images side-by-side.

    Parameters
    ----------
    images : list of 2-D arrays
    titles : list of str
    """
    n = len(images)
    if figsize is None:
        figsize = (4 * n, 4)
    fig, axes = plt.subplots(1, n, figsize=figsize)
    if n == 1:
        axes = [axes]
    if titles is None:
        titles = [''] * n

    ims = []
    for ax, img, title in zip(axes, images, titles):
        im = ax.imshow(img, cmap=cmap, origin='lower')
        ax.set_title(title)
        ax.set_xlabel('x (px)')
        ax.set_ylabel('y (px)')
        ims.append(im)

    if colorbar:
        for ax, im in zip(axes, ims):
            fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    if suptitle:
        fig.suptitle(suptitle, fontsize=13, y=1.02)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# PCA helpers
# ---------------------------------------------------------------------------

def plot_scree(explained_variance_ratio, n_show=20, ax=None):
    """Scree plot (explained variance by component)."""
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 3))
    n = min(n_show, len(explained_variance_ratio))
    cumulative = np.cumsum(explained_variance_ratio[:n]) * 100
    ax.bar(range(1, n + 1), explained_variance_ratio[:n] * 100,
           color='steelblue', alpha=0.8, label='Individual')
    ax.plot(range(1, n + 1), cumulative, 'o-', color='coral',
            label='Cumulative', ms=4)
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained variance (%)')
    ax.set_title('Scree Plot')
    ax.legend(fontsize=9)
    ax.set_xlim(0.5, n + 0.5)
    ax.grid(axis='y', alpha=0.3)
    return ax


def plot_component_maps(component_maps, n_show=4, figsize=None, cmap='RdBu_r'):
    """
    Show spatial maps of the first n_show PCA components.

    Parameters
    ----------
    component_maps : ndarray, shape (n_components, n_x, n_y)
    """
    n_show = min(n_show, component_maps.shape[0])
    if figsize is None:
        figsize = (4 * n_show, 4)
    fig, axes = plt.subplots(1, n_show, figsize=figsize)
    if n_show == 1:
        axes = [axes]
    for i, ax in enumerate(axes):
        vmax = np.abs(component_maps[i]).max()
        im = ax.imshow(component_maps[i], cmap=cmap, origin='lower',
                       vmin=-vmax, vmax=vmax)
        ax.set_title(f'PC {i + 1}')
        ax.axis('off')
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.suptitle('PCA Component Maps', fontsize=13)
    fig.tight_layout()
    return fig


def plot_spectra_comparison(freq, spectra_dict, title='Spectra', ylabel='Intensity'):
    """
    Overlay multiple sets of spectra on one plot.

    Parameters
    ----------
    spectra_dict : dict  {label: array_of_shape_(n_spectra, n_freq)}
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = plt.cm.tab10.colors
    for idx, (label, spectra) in enumerate(spectra_dict.items()):
        spectra = np.atleast_2d(spectra)
        c = colors[idx % len(colors)]
        for s in spectra:
            ax.plot(freq, s, color=c, alpha=0.5, lw=1)
        ax.plot(freq, spectra.mean(axis=0), color=c, lw=2, label=label)
    ax.set_xlabel('Frequency / Energy (a.u.)')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Clustering helpers
# ---------------------------------------------------------------------------

def plot_cluster_map(labels, n_clusters=None, title='Cluster map',
                     ax=None, figsize=(5, 5)):
    """Display cluster label image with a discrete colorbar."""
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    if n_clusters is None:
        n_clusters = int(labels.max()) + 1
    cmap = plt.cm.get_cmap('tab10', n_clusters)
    im = ax.imshow(labels, cmap=cmap, origin='lower',
                   vmin=-0.5, vmax=n_clusters - 0.5)
    ax.set_title(title)
    ax.axis('off')
    cb = fig.colorbar(im, ax=ax, ticks=range(n_clusters),
                      fraction=0.046, pad=0.04)
    cb.set_label('Cluster')
    return fig, ax


# ---------------------------------------------------------------------------
# Sparse sampling helpers
# ---------------------------------------------------------------------------

def plot_sampling_overview(target, mask, reconstruction, error_map,
                           figsize=(14, 4)):
    """
    Four-panel figure: target | sampled | reconstruction | error.
    """
    fig, axes = plt.subplots(1, 4, figsize=figsize)

    axes[0].imshow(target, cmap='viridis', origin='lower')
    axes[0].set_title('Ground Truth')

    sampled = np.full_like(target, np.nan)
    sampled[mask] = target[mask]
    axes[1].imshow(sampled, cmap='viridis', origin='lower')
    axes[1].set_title(f'Sampled ({mask.sum()} pts,\n'
                      f'{100*mask.mean():.1f}%)')

    axes[2].imshow(reconstruction, cmap='viridis', origin='lower')
    axes[2].set_title('Reconstruction')

    vmax = np.abs(error_map).max()
    im = axes[3].imshow(error_map, cmap='RdBu_r', origin='lower',
                        vmin=-vmax, vmax=vmax)
    axes[3].set_title('Error')
    fig.colorbar(im, ax=axes[3], fraction=0.046, pad=0.04)

    for ax in axes:
        ax.axis('off')
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Autonomous measurement helpers
# ---------------------------------------------------------------------------

def plot_adaptive_state(target, sampled_mask, model_mean, uncertainty,
                        next_point=None, step=None, figsize=(14, 4)):
    """
    Four-panel figure for one step of the adaptive loop.
    target | sampled pixels | GP/model mean | uncertainty + next point
    """
    fig, axes = plt.subplots(1, 4, figsize=figsize)

    axes[0].imshow(target, cmap='viridis', origin='lower')
    axes[0].set_title('Ground Truth')

    obs = np.full_like(target, np.nan)
    obs[sampled_mask] = target[sampled_mask]
    axes[1].imshow(obs, cmap='viridis', origin='lower')
    axes[1].set_title(f'Measurements\n(n={sampled_mask.sum()})')

    axes[2].imshow(model_mean, cmap='viridis', origin='lower')
    axes[2].set_title('Model Estimate')

    im = axes[3].imshow(uncertainty, cmap='hot', origin='lower')
    axes[3].set_title('Uncertainty\n(next target in blue)')
    fig.colorbar(im, ax=axes[3], fraction=0.046, pad=0.04)

    if next_point is not None:
        axes[3].plot(next_point[1], next_point[0], 'b*', ms=14,
                     label='Next point')
        axes[3].legend(fontsize=8)

    for ax in axes:
        ax.axis('off')

    title = f'Adaptive Measurement — Step {step}' if step is not None else \
            'Adaptive Measurement'
    fig.suptitle(title, fontsize=13)
    fig.tight_layout()
    return fig
