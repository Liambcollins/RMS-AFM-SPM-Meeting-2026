# Exercise 04 — Autonomous SPM

**Notebook:** `04_autonomous_spm.ipynb`

---

## Tasks

### 1. Change the number of seed measurements
Try `n_seed = 4`, `16`, and `32`.
- How does the initial model quality change?
- Does the adaptive loop still converge well with very few seeds?

### 2. Change the acquisition function weighting
In the `acquisition_function` call, try `alpha=1.0` (pure uncertainty) and `alpha=0.0` (pure gradient).
- Does one perform better than the other?
- Why might you want a mixture of both?

### 3. More adaptive steps
Increase `N_steps` from 40 to 100.
- Does the RMSE continue to decrease, or does it plateau?
- Where does the instrument measure after most of the image has been sampled?

### 4. Change the decay parameter
The `distance_uncertainty` function has a `decay` parameter (default 4.0).
- Try `decay=1.0` (short range) and `decay=15.0` (long range).
- How does this affect where the next measurement is placed?

### 5. (Stretch) Compare final RMSE curves
Run the adaptive loop 3 times with different random seeds (`rng = np.random.default_rng(0)`, `1`, `2`).
- How consistent is the final RMSE?
- What is the variance in performance?

### 6. (Stretch) Different target images
Generate a different target with `make_adaptive_target(random_state=99)`.
- Does the adaptive loop still perform well?
- Are there target types where the simple uncertainty model fails?

---

**Tip:** The toy adaptive loop in this notebook is conceptually identical to real autonomous SPM systems — the difference is that real systems call instrument control software to take the measurement, rather than reading from a pre-computed array.
