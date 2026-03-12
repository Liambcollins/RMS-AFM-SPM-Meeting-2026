# Exercise 01 — PCA Denoising

**Notebook:** `01_pca_denoising.ipynb`

---

## Tasks

### 1. Scree plot interpretation
Run the PCA on the synthetic hyperspectral cube and look at the scree plot.
- How many components would you retain to capture most of the signal?
- At what component does the curve level off?

### 2. Change the noise level
Go back to the `make_hyperspectral_spm` call and increase `noise_level` from `0.3` to `0.8`.
- How does the scree plot change?
- Do you need more or fewer components to reconstruct well?

### 3. Reconstruction quality
Try reconstructing the cube with 1, 2, 3, and 10 components.
- Which reconstruction looks best visually?
- Does the RMSE curve agree with your visual judgement?

### 4. Component maps
Look at the first three component maps.
- Do they correspond to the three spatial domains you would expect?
- What do the later component maps (e.g. PC 5, PC 10) look like?

### 5. (Stretch) More components
Change `n_components=3` to `n_components=5` in `make_hyperspectral_spm`.
- How does this change the PCA results?
- Can you still identify the components cleanly?

---

**Tip:** The key insight is that real signal concentrates in the first few components, while noise is spread across many components. Reconstruction with a small number of PCs is a simple and powerful denoiser.
