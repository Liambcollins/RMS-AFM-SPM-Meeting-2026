# Exercise 03 — Sparse & Smart Measurements

**Notebook:** `03_sparse_smart_measurements.ipynb`

---

## Tasks

### 1. Change the sampling fraction
Try `fraction = 0.02`, `0.05`, `0.20`, and `0.50` in the random sampling cell.
- At what fraction does the reconstruction become visually acceptable?
- Look at the error map — where are the largest errors?

### 2. Compare grid vs random at the same budget
Set the grid stride so that `mask_grid.mean()` is approximately equal to your chosen `fraction`.
- Does grid or random sampling give a better reconstruction?
- Why might one be better than the other for this type of image?

### 3. Change the target image type
Go back to `make_sparse_target_image` and try `feature_type='smooth'` and `feature_type='edges'`.
- Does sparse sampling work better on smooth or edge-heavy images? Why?

### 4. RBF vs cubic spline
Compare `reconstruct_griddata(method='cubic')` and `reconstruct_rbf(...)` on the same sparse mask.
- Which gives lower RMSE?
- Are there artefacts near the edges of the image with either method?

### 5. (Stretch) Gradient-guided sampling
Experiment with the gradient-guided sampling cell.
- Increase or decrease `n_extra` to change the budget.
- Change `gaussian_filter(sigma=...)` to control how smooth the gradient map is.
- Does gradient-guided sampling reliably beat random at the same budget?

---

**Tip:** The benefit of smart sampling is most obvious for images with localised features (sharp edges, narrow peaks). Smooth images can be well reconstructed with simple grid or random sampling.
