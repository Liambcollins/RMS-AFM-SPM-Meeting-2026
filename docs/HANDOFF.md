# Handoff — ML/AI in SPM tutorial (RMS AFM & SPM Meeting 2026)

Short status doc so any new session/account can continue. **The repo folder is the source of truth** — everything below is already saved here.

## Deliverables (in repo root)

| File | What it is |
|------|-----------|
| `ML_SPM_Tutorial_ORNL.pptx` | Main ~27-slide talk (~25–30 min), ORNL template, repo QR on the agenda + closing slides. Speaker notes embedded in every slide. |
| `ML_Progression_Linear_to_CNN_ORNL.pptx` | 5-slide stack: linear → logistic → neural nets → CNN (overview + 4 concept slides). |
| `ML_Unsupervised_ORNL.pptx` | 5-slide stack: clustering (force-volume) · dimensionality reduction · denoising · PCA-hub synthesis. |
| `Sparse_Sampling_ORNL.pptx` | 3-slide stack: spiral+GP (+uncertainty) → 15/25/50% coverage sweep → random+RBF, leading into Autonomous SPM. |
| `docs/talk_script.md` | Full timed speaker script for the main deck (~29 min). |

All decks use the ORNL template (13.33×7.5, Aptos font, ORNL green `#00662C`). Standalone stacks are styled to drop straight into the main deck.

## Repo changes made

- **Notebooks (`notebooks/`)** — all core `00`–`08` are pre-run with figures embedded (so they render on phones via GitHub/nbviewer) and have a Colab-bootstrap first cell. Added runnable sections: logistic regression (`05`), CNN/convolution demo (`07`), force-volume clustering (`02`), spiral+GP & coverage sweep (`03`). Rewrote the broken `optional/08_manifold_learning` into a real PCA/t-SNE notebook. Optional `08→10` renumbered. Fixed real bugs in `00` and `01` (bad API calls, NumPy-2 `.ptp()`).
- **`src/`** — new generators: `make_fd_curve`, `make_modulus_dataset`, `make_scan_quality_dataset`, `make_force_volume` (in `synthetic/generators.py`); new `spiral_mask` + `reconstruct_gp` (in `ml/reconstruction.py`).
- **`figures/`** — all slide figures generated from the repo's own code. `.gitignore` whitelists `fig_*.png`, `qr_repo.png`, `rung_*.png`, `uns_*.png`.
- **`README.md`** — corrected repo URL, per-notebook "Run in Colab" + "View on nbviewer" links, run-vs-view-on-phone guidance.
- **QR code** — `figures/qr_repo.png` → `https://github.com/Liambcollins/RMS-AFM-SPM-Meeting-2026` (verified by decode).

## Still pending / next steps

1. **Commit & push** — none of this is committed yet. The QR / Colab / nbviewer links only go live once pushed to `github.com/Liambcollins/RMS-AFM-SPM-Meeting-2026` (`git add . && git commit && git push`).
2. **Splice standalone stacks into the main deck** (optional) — the 3 standalone `.pptx` stacks are not yet merged into `ML_SPM_Tutorial_ORNL.pptx`; the main deck still shows the original single sparse-sampling slide. Merging would require renumbering the master speaker script too.
3. **Optional notebooks `09`/`10`** are illustrative scaffolds, not pre-rendered.

## Notes / gotchas

- Build scripts were written in the session scratch (`/tmp`) and are not in the repo; decks are rebuilt by regenerating figures + re-running the builder. The `.pptx` files themselves are final.
- Force-volume clustering: cluster on the curve **magnitude** (PCA of raw curves, *not* per-feature standardized) — magnitude encodes stiffness.
- Synthetic force/modulus values assume soft-matter (Poisson 0.5, kPa moduli) — adjust for hard materials.
