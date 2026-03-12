# RMS AFM & SPM Meeting 2026
This repository accompanies the Machine Learning in Scanning Probe Microscopy tutorial presented at the RMS AFM & SPM Meeting 2026.


Machine Learning for Scanning Probe Microscopy
1. PCA for SPM Denoising and Dimensionality Reduction

Start with this because it is intuitive and extremely powerful for SPM datasets.

Topics:

PCA basics (covariance, eigenvectors)

Denoising hyperspectral SPM datasets

Reducing dimensionality in spectroscopy data (BE-PFM, G-mode, KPFM)

Interpreting principal components physically

Example datasets:

Band excitation spectra

Force–distance curves

KPFM frequency sweeps

Outcome:

Demonstrate how low-rank structure reveals signal vs noise

2. Unsupervised Clustering of SPM Data

Natural next step after PCA.

Methods:

K-Means

Gaussian Mixture Models

DBSCAN

Applications:

Domain segmentation in PFM

Phase separation in membranes / polymers

Identifying regions of similar spectroscopy behavior

Example:

Cluster hyperspectral maps → reveal hidden material phases.

Key message:
ML can reveal structure in high-dimensional SPM data that traditional thresholding misses.

3. Nonlinear Embedding & Manifold Learning

This is extremely powerful for spectroscopy datasets.

Methods:

t-SNE

UMAP

Diffusion maps

Applications:

Visualization of high-dimensional spectroscopy

Identifying trajectories in hysteresis loops

Discovering hidden physical states

Key point:
Many SPM datasets live on low-dimensional nonlinear manifolds.

4. ML Denoising Beyond PCA

This ties directly into your “sub-noise-floor AFM” idea.

Methods:

Autoencoders

Denoising autoencoders

Wavelet + ML hybrid approaches

Self-supervised denoising (Noise2Noise / Noise2Void)

Applications:

Denoising G-mode cantilever signals

Removing structured noise

Recovering weak electromechanical signals

5. Image Segmentation with Deep Learning

Very practical for SPM users.

Methods:

U-Net

Random forest pixel classification

Feature-based segmentation

Applications:

Ferroelectric domain segmentation

Grain boundaries

Biological membranes

Tip artifacts

Example:
Train segmentation on SimuScan or synthetic AFM data.

6. Physics-Informed ML for Spectroscopy

Very relevant to the SPM community.

Examples:

SHO parameter extraction with ML

ML-assisted fitting of force curves

Neural networks for rapid parameter inference

Applications:

BE-PFM fitting

Contact resonance analysis

Electrochemical impedance spectra

Message:
ML can replace expensive nonlinear fitting loops.

7. Active Learning for Smart Measurements

This connects directly to the future of SPM.

Methods:

Bayesian optimization

Active learning

Uncertainty sampling

Applications:

Selecting next measurement location

Adaptive spectroscopy

Learning optimal excitation conditions

Example:
AFM chooses where to measure next based on model uncertainty.

8. Autonomous SPM Workflows

This is a strong closing topic.

Concept:
Closed-loop ML-driven experiments.

Architecture:

SPM Measurement
       ↓
Real-time ML analysis
       ↓
Decision engine
       ↓
Next measurement chosen

Examples:

Adaptive spectroscopy

Autonomous domain mapping

Automated tip conditioning

Real-time feature tracking

Tie into:

G-mode AFM

Fast hyperspectral imaging

Autonomous laboratories

9. Fast & High-Resolution Measurements with ML

Explain the emerging paradigm:

Instead of measuring everything → measure sparsely and reconstruct.

Methods:

Compressive sensing

Sparse sampling

Neural field reconstruction

Applications:

Faster AFM imaging

Sparse spectroscopy grids

Hyperspectral reconstruction
