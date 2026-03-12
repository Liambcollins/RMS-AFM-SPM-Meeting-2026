<<<<<<< Updated upstream
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Machine Learning in Scanning Probe Microscopy</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
html {scroll-behavior:smooth}
</style>
</head>

<body class="bg-slate-950 text-slate-100">

<!-- HERO -->
<section class="relative overflow-hidden border-b border-white/10">

<div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(56,189,248,0.18),transparent_28%),radial-gradient(circle_at_left,rgba(168,85,247,0.18),transparent_30%),linear-gradient(to_bottom,rgba(15,23,42,0.96),rgba(2,6,23,1))]"></div>

<div class="relative mx-auto max-w-7xl px-6 py-24">

<div class="grid lg:grid-cols-2 gap-12 items-center">

<div>

<div class="mb-4 inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-cyan-400/10 px-3 py-1 text-xs uppercase tracking-widest text-cyan-200">
RMS AFM & SPM Meeting 2026
</div>

<h1 class="text-5xl font-semibold leading-tight">
Machine Learning in<br>
<span class="text-cyan-300">Scanning Probe Microscopy</span>
</h1>

<p class="mt-6 text-lg text-slate-300 max-w-xl">
A hands‑on tutorial exploring how machine learning enables smarter
SPM workflows — from PCA denoising and clustering to fast,
adaptive, and autonomous measurements.
</p>

<div class="mt-8 flex gap-4">
<a href="#modules" class="bg-cyan-400 text-slate-950 px-6 py-3 rounded-xl font-semibold hover:bg-cyan-300">
Explore Modules
</a>

<a href="#repo" class="border border-white/20 px-6 py-3 rounded-xl hover:bg-white/10">
Repository Overview
</a>
</div>

<div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-10">

<div class="bg-white/5 border border-white/10 p-4 rounded-xl">
<div class="font-semibold">PCA</div>
<div class="text-sm text-slate-400">Denoising</div>
</div>

<div class="bg-white/5 border border-white/10 p-4 rounded-xl">
<div class="font-semibold">Clustering</div>
<div class="text-sm text-slate-400">Phase mapping</div>
</div>

<div class="bg-white/5 border border-white/10 p-4 rounded-xl">
<div class="font-semibold">Smart</div>
<div class="text-sm text-slate-400">Measurements</div>
</div>

<div class="bg-white/5 border border-white/10 p-4 rounded-xl">
<div class="font-semibold">Autonomous</div>
<div class="text-sm text-slate-400">SPM</div>
</div>

</div>

</div>


<!-- HERO GRAPHIC -->

<div class="bg-slate-900 border border-white/10 rounded-2xl p-4">

<svg viewBox="0 0 720 520" class="w-full">

<defs>

<linearGradient id="surface" x1="0" x2="1">
<stop offset="0%" stop-color="#22d3ee"/>
<stop offset="50%" stop-color="#34d399"/>
<stop offset="100%" stop-color="#a855f7"/>
</linearGradient>

</defs>

<rect x="0" y="0" width="720" height="520" rx="20" fill="#020617"/>

<!-- cantilever -->

<path d="M120 120 L380 120 L440 180" stroke="#e2e8f0" stroke-width="16" stroke-linecap="round" fill="none"/>

<path d="M440 180 L470 260" stroke="#e2e8f0" stroke-width="10" stroke-linecap="round" fill="none"/>

<polygon points="462,260 478,260 470,282" fill="white"/>

<!-- surface -->

<rect x="140" y="320" width="460" height="90" rx="18" fill="#0f172a" stroke="#334155"/>

<path
 d="M160 370 C200 340 240 340 280 370 S360 400 400 370 S480 340 520 370"
 fill="none"
 stroke="url(#surface)"
 stroke-width="12"
 stroke-linecap="round"
/>

<!-- labels -->

<text x="40" y="50" fill="#cbd5e1" font-size="18">ML‑Enhanced SPM Workflow</text>

</svg>

</div>

</div>

</div>

</section>


<!-- REPO -->

<section id="repo" class="max-w-7xl mx-auto px-6 py-20">

<h2 class="text-3xl font-semibold">Repository Overview</h2>

<p class="mt-6 text-slate-300 max-w-3xl">
This repository accompanies the
<b>Machine Learning in Scanning Probe Microscopy</b>
tutorial at the RMS AFM & SPM Meeting 2026.

It contains notebooks, synthetic datasets, and example
workflows demonstrating how machine learning can enhance
modern SPM experiments.
</p>


<div class="grid sm:grid-cols-2 gap-6 mt-10">

<div class="bg-slate-900 border border-white/10 p-6 rounded-xl">
<h3 class="font-semibold">Portable demos</h3>
<p class="text-sm text-slate-400 mt-2">
Synthetic SPM‑like datasets allow examples to run anywhere
without proprietary file formats.
</p>
</div>

<div class="bg-slate-900 border border-white/10 p-6 rounded-xl">
<h3 class="font-semibold">Notebook‑first</h3>
<p class="text-sm text-slate-400 mt-2">
Interactive Jupyter notebooks provide visual explanation
and runnable demonstrations.
</p>
</div>

<div class="bg-slate-900 border border-white/10 p-6 rounded-xl">
<h3 class="font-semibold">Practical ML</h3>
<p class="text-sm text-slate-400 mt-2">
Examples focus on real SPM problems including noisy
hyperspectral data and domain mapping.
</p>
</div>

<div class="bg-slate-900 border border-white/10 p-6 rounded-xl">
<h3 class="font-semibold">Future SPM</h3>
<p class="text-sm text-slate-400 mt-2">
Later modules explore smart measurements and
adaptive microscopy workflows.
</p>
</div>

</div>

</section>


<!-- MODULES -->

<section id="modules" class="max-w-7xl mx-auto px-6 py-20">

<h2 class="text-3xl font-semibold">Tutorial Modules</h2>

<p class="mt-4 text-slate-300 max-w-3xl">
The tutorial progresses from simple ML tools to
advanced autonomous measurement concepts.
</p>

<div class="grid lg:grid-cols-2 gap-8 mt-12">

<div class="bg-white/5 border border-white/10 p-6 rounded-xl">
<h3 class="text-xl font-semibold">01 — PCA Denoising</h3>
<p class="mt-3 text-slate-400">
Use dimensionality reduction to separate signal from noise
in hyperspectral SPM datasets.
</p>
</div>

<div class="bg-white/5 border border-white/10 p-6 rounded-xl">
<h3 class="text-xl font-semibold">02 — Clustering & Phase Mapping</h3>
<p class="mt-3 text-slate-400">
Automatically discover domains and material regions
using unsupervised learning.
</p>
</div>

<div class="bg-white/5 border border-white/10 p-6 rounded-xl">
<h3 class="text-xl font-semibold">03 — Sparse Measurements</h3>
<p class="mt-3 text-slate-400">
Demonstrate how fewer measurements can still
recover spatial structure.
</p>
</div>

<div class="bg-white/5 border border-white/10 p-6 rounded-xl">
<h3 class="text-xl font-semibold">04 — Autonomous SPM</h3>
<p class="mt-3 text-slate-400">
Introduce adaptive measurement loops
for intelligent microscopy.
</p>
</div>

</div>

</section>


<!-- FOOTER -->

<section class="border-t border-white/10 py-12">

<div class="max-w-7xl mx-auto px-6 flex flex-col lg:flex-row justify-between items-center gap-6">

<div>
<div class="font-semibold text-lg">RMS AFM & SPM 2026 Tutorial</div>
<div class="text-sm text-slate-400">Machine Learning for Scanning Probe Microscopy</div>
</div>

<div class="flex gap-4">
<a href="#" class="border border-white/20 px-4 py-2 rounded-lg hover:bg-white/10">View Repo</a>
<a href="#modules" class="bg-cyan-400 text-slate-950 px-4 py-2 rounded-lg">Start Tutorial</a>
</div>

</div>

</section>

</body>
</html>
=======
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
├── docs/               # Documentation and notes
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
>>>>>>> Stashed changes
