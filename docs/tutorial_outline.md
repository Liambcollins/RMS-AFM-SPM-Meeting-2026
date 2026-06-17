# Tutorial Outline

**Machine Learning & AI in Scanning Probe Microscopy**
*RMS AFM & SPM Meeting 2026*
*Liam Collins*

---

## Overview

A big-picture, practical tour of machine learning and AI for SPM. The talk is ~25–30 minutes; the
repository goes deeper for self-paced study. We prioritise intuition over derivations, and all core
examples run on synthetic data so no instrument access is required.

---

## Core modules

| # | Module | Idea |
|---|--------|------|
| 00 | Setup & Overview | Why ML for SPM; SPM data types; environment check |
| 01 | PCA Denoising | Separate signal from noise in hyperspectral cubes |
| 02 | Clustering & Phase Mapping | Find phases/domains without labels (KMeans, GMM) |
| 03 | Sparse & Smart Measurements | Reconstruct images from few points; sample where it matters |
| 04 | Autonomous SPM | Closed-loop adaptive measurement vs. random sampling |
| 05 | Regression: Calibration | Predict numbers — Hertzian fit, modulus from F–D features |
| 06 | Classification: Scan QC | Predict labels — good/bad scans; confusion matrix, precision/recall |
| 07 | Neural Networks | From linear models to MLPs and CNNs; when deep learning pays off |

## Real-data showcase

- **Annexin V HS-AFM** — dimensionality reduction, denoising, clustering and dynamics mapping on a
  published High-Speed AFM dataset of protein assembly on a lipid bilayer.

## Optional / advanced modules

| # | Module | Idea |
|---|--------|------|
| 08 | Manifold Learning | t-SNE / UMAP for hyperspectral SPM data |
| 09 | Image Segmentation | Otsu, watershed, SLIC superpixels |
| 10 | Physics-Informed ML | Embedding physical models (Lorentzian, contact mechanics) |

## Frontier (discussion)

- **Foundation models & LLMs** as analysis copilots and literature/metadata miners
- **Generative AI** for data augmentation, denoising and inverse design
- **Agents & self-driving labs** — autonomous experiment planning and execution

---

## Suggested talk arc

Supervised basics (05 → 06) → neural nets (07) → unsupervised tools (01 → 02) →
smarter measurement (03 → 04) → real data (Annexin) → frontier (LLMs / generative / agents).

## Prerequisites

- Basic Python (numpy, matplotlib)
- No prior ML knowledge assumed
- No SPM instrumentation required
