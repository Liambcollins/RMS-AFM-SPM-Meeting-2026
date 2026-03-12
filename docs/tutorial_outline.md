# Tutorial Outline

**Machine Learning in Scanning Probe Microscopy**
*RMS AFM & SPM Meeting 2026*
*Liam Collins*

---

## Overview

This tutorial introduces machine learning methods that are directly applicable to SPM data analysis. The focus is practical and visual — we prioritise intuition over derivations, and all examples run on synthetic data so no instrument access is required.

Estimated total time: ~3–4 hours (workshop) or self-paced.

---

## Module 00 — Setup & Overview (~20 min)
- Why ML for SPM?
- SPM data types: images, spectra, hyperspectral cubes
- Overview of the tutorial modules
- Environment check and imports

## Module 01 — PCA Denoising (~45 min)
- Intuitive introduction to PCA
- Generating synthetic hyperspectral data
- Scree plots and component maps
- PCA reconstruction and denoising
- Comparing reconstruction quality

## Module 02 — Clustering & Phase Mapping (~45 min)
- Why clustering for SPM?
- PCA preprocessing
- KMeans clustering and cluster maps
- Gaussian Mixture Models (soft clustering)
- Choosing the number of clusters (elbow, silhouette)

## Module 03 — Sparse & Smart Measurements (~45 min)
- The measurement speed problem in SPM
- Random and grid sparse sampling
- Reconstruction from sparse data
- Gradient-guided smart sampling
- Reconstruction quality vs measurement budget

## Module 04 — Autonomous SPM (~45 min)
- Closed-loop measurement concepts
- Uncertainty and acquisition functions
- The adaptive measurement loop (toy implementation)
- Comparing adaptive vs random sampling
- Discussion of real-world implementations

---

## Optional Modules

### Module 05 — Manifold Learning
t-SNE and UMAP for visualising hyperspectral SPM data in 2D.

### Module 06 — Image Segmentation
Thresholding, watershed, and superpixel methods for SPM images.

### Module 07 — Physics-Informed ML
Embedding physical models (Lorentzian, contact mechanics) into ML pipelines.

---

## Prerequisites

- Basic Python (numpy, matplotlib)
- No prior ML knowledge assumed
- No SPM instrumentation required
