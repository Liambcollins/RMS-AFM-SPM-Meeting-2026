# Exercise 02 — Clustering & Phase Mapping

**Notebook:** `02_clustering_phase_mapping.ipynb`

---

## Tasks

### 1. Try different numbers of clusters
Re-run KMeans with `n_clusters=2`, `4`, and `6`.
- Which number of clusters gives the most meaningful phase map?
- Look at the elbow and silhouette plots — do they agree with your visual impression?

### 2. Skip the PCA step
Modify the clustering cell so that it uses the raw spectral features (the full 64-channel cube flattened) instead of PCA scores.
- Is the result better or worse?
- How does the computation time change?

### 3. GMM vs KMeans
Compare the KMeans and GMM cluster maps side by side.
- Where do they agree? Where do they disagree?
- Look at the GMM soft probabilities — which pixels are most uncertain?

### 4. Change the noise level
Go back to `make_hyperspectral_spm` and try `noise_level=0.05` (low noise) and `noise_level=0.6` (high noise).
- How does clustering quality change?
- At what noise level does clustering break down?

### 5. (Stretch) Custom colourmap
The default cluster colourmap is `tab10`. Try plotting the cluster map with a different colourmap.
- Which colourmap best reveals the phase structure?

---

**Tip:** Clustering works best after noise reduction (e.g. PCA preprocessing). High noise can cause clusters to reflect noise rather than real phases.
