# Speaker Script — Machine Learning & AI in Scanning Probe Microscopy

*RMS AFM & SPM Meeting 2026 · Tutorial Session · Liam Collins*

**Target length: ~29 minutes** (25–30 min talk). Timings are per slide; pad or trim the Part dividers and the toolchain/pitfalls slides to hit your exact slot. The script is also embedded in each slide's Notes pane in `ML_SPM_Tutorial_ORNL.pptx`.

**Sum of slide timings: 29 min 0 s.**

---

## Slide 1 — Title — Machine Learning & AI in SPM  
*(0:45)*

Good morning, and thank you all for coming. Over the next half hour I want to give you a practical, big-picture tour of how machine learning — and now AI more broadly — is being used in scanning probe microscopy. I'm deliberately not going to drown you in equations. The goal is intuition: what these methods actually do, where they pay off in a real SPM workflow, and how you can start using them yourself today. Everything I show is backed by a runnable notebook, and I'll point you to all of it. I'm Liam Collins from Oak Ridge — I work on functional imaging and automated microscopy. Let's get into it.

## Slide 2 — Agenda + QR — What we'll cover  
*(1:15)*

Here's the plan: five short parts. First the big picture — what ML really is, and why SPM is such fertile ground for it. Then supervised learning, where we predict numbers and labels. Then unsupervised learning, where we find structure with no labels at all. Then using ML to measure smarter — sparse and autonomous microscopy. And finally a quick look at the frontier: large language models, generative AI, and agents. Now — the single most useful thing on this slide is the QR code on the right. Every example I show today is a Jupyter notebook in this GitHub repo. If you have a laptop, you can run them in your browser through Colab with no installation. If you only have your phone, the notebooks are pre-run with every figure saved inside, so you can just read along. Feel free to scan it now; it'll also be on the final slide.

## Slide 3 — PART 1 divider — The big picture  
*(0:15)*

So, part one — the big picture. What machine learning is, and why scanning probe microscopy needs it.

## Slide 4 — What is ML — examples, not rules  
*(1:30)*

Let's demystify the term. The core idea of machine learning is this: you teach a computer with examples, not with rules. Think about how you learned to spot a bad scan. Nobody handed you a rulebook. You looked at hundreds, maybe thousands of images, and your brain gradually learned the pattern — this one's clean, this one's a tip crash. Machine learning does exactly the same thing: you show it examples, and it finds the pattern — but faster, at scale, and without getting tired or inconsistent. Now let me kill four myths up front, because they trip people up. It's not magic — it's statistics and optimization. You don't always need big data — plenty of methods work well with a few hundred samples. It doesn't replace scientists — it augments your judgment. And fancier is not always better — for small datasets a simple model usually wins. Keep that last one in mind; we'll come back to it.

## Slide 5 — Three flavors of ML  
*(1:30)*

There are three broad flavors of machine learning, and each maps onto a different kind of SPM problem. Supervised learning is when you give the model labeled examples — this scan is good, this one is bad — and it learns to predict the label. That covers classification and regression, and it's most of part two. Unsupervised learning is when you have no labels; you just ask the model to find hidden structure. In SPM that's things like, what phase clusters exist in my map? That's clustering and dimensionality reduction, which is part three. And self-supervised learning sits in between — the model learns from the structure of the data itself, which is powerful for things like anomaly detection: flagging the unusual region without ever being told what unusual looks like. Don't memorize the boxes — just remember: do I have labels or not? That single question points you to the right family of methods.

## Slide 6 — Why SPM data is ML-shaped  
*(1:15)*

So why is SPM such a natural fit for this? Look at what our data is actually like. First, it's high-dimensional — topography, phase, amplitude, potential, often all collected at once in multi-channel stacks. Second, it's full of artifacts — tip crashes, streak noise, thermal drift, contamination — and each of those looks different. Third, human labeling is genuinely hard and inconsistent: what looks like a domain wall to me might look like noise to you, and that disagreement only grows as datasets get bigger. And fourth, modern workflows generate huge scan counts — parameter sweeps, voltage maps, temperature series — easily hundreds of images per experiment. Every one of those is a problem humans struggle to handle at scale, and exactly where ML earns its keep.

## Slide 7 — The ML pipeline  
*(1:15)*

Here's the reassuring part. Every ML project, no matter how fancy, follows the same six-step pipeline. You start with raw data and load it. You preprocess — flatten, destripe, normalize. You either hand-label it or extract features. You train on part of the data and validate on another part. You evaluate honestly with the right metrics. And then you deploy and extend — run it on new data, iterate, share it. Learn this loop once and it transfers everywhere — from a five-line classifier to a deep neural network. Every notebook in the repo walks through this exact sequence, so once you've seen one, the rest feel familiar.

## Slide 8 — Overfitting  
*(1:30)*

If you take only one technical concept away today, make it this one: overfitting. A model that simply memorizes your training data will look brilliant on that data and then fail completely on the next scan. The defense is simple and non-negotiable: always split your data. Train on the bulk of it, hold out a validation set to tune your settings, and keep a test set locked away for one final, honest check. The three pictures at the bottom capture the whole story. Underfitting: the model's too simple, high error everywhere. Overfitting: it's memorized the training set, near-zero error there but high error on new data. And in between, the sweet spot — a model that generalizes. Almost everything that goes wrong in applied ML is some version of overfitting, so build the habit now.

## Slide 9 — PART 2 divider — Supervised learning  
*(0:15)*

That's the foundation. Part two: supervised learning — predicting a number, and predicting a label.

## Slide 10 — Regression  
*(1:30)*

Let's start with regression, which just means predicting a continuous number. This is everywhere in SPM — adhesion, stiffness, modulus, calibration factors. The plot on the left is a force-distance curve, and here's the trick I love: the physics is non-linear — Hertzian contact goes as indentation to the three-halves power — but if I use indentation-to-the-three-halves as my feature, the relationship becomes a straight line, and a one-line linear fit recovers the modulus. That's feature engineering guided by physics, and it's one of the most powerful moves you have. On the right, we scale up: extract a few features from hundreds of curves and train a model to predict Young's modulus directly. The predicted-versus-true points hug the diagonal — that's a good model. This is notebook 05, and it runs in seconds.

## Slide 11 — Classification  
*(1:30)*

Classification is the sibling problem: instead of a number, you predict a category. The motivating example here is automated scan quality control — is this scan good or bad? Do it by hand across hundreds of images and it's slow and inconsistent; a classifier does it in seconds, the same way every time. The left panel shows a logistic regression — the simplest classifier — drawing a straight boundary between good and bad scans based on two features. Start there: it's fast and interpretable. The right panel is the part I want to hammer home: evaluation. Never report accuracy alone. If ninety-nine percent of your scans are good, a model that blindly says 'good' every time is ninety-nine percent accurate and totally useless, because it never catches a crash. So we look at the confusion matrix and at precision and recall for the rare class. That's notebook 06.

## Slide 12 — Neural networks  
*(1:30)*

So when do you reach for a neural network? When straight lines aren't enough. A linear model draws one straight boundary. A neural network stacks many simple non-linear units in layers, and that lets it bend and fold the boundary to fit complex patterns — you can see the difference between the linear fit and the neural net on these two panels. The curve on the right is the training loss going down as it learns. For images specifically — which is most SPM data — the workhorse is the convolutional neural network, or CNN: it slides learnable filters across the image to pick up edges, domain walls, defects. CNNs power the heavy tasks — segmentation, denoising, defect detection — usually built in PyTorch. But here's the honest caveat, and it's that 'simpler is often better' point again: deep networks need a lot of data. With a few hundred samples, a well-chosen feature plus a random forest will frequently beat a neural net. Match the model to the dataset, not to the hype. Notebook 07.

## Slide 13 — PART 3 divider — Unsupervised learning  
*(0:15)*

Now flip it around. Part three: unsupervised learning — finding structure when you have no labels at all.

## Slide 14 — PCA  
*(1:30)*

The workhorse of unsupervised SPM analysis is PCA — principal component analysis. The idea is intuitive: PCA finds the dominant, repeating patterns in your data and orders them from most to least important. The single biggest use is denoising hyperspectral data. On the left is a raw, noisy frame. In the middle, the same frame reconstructed from just the first three principal components — dramatically cleaner, but the real features are preserved. How did I know to keep three? The scree plot on the right. You look for the 'elbow' — the point where the curve flattens out. Components before the elbow are real signal; everything after is noise. Here the elbow is right at three, which makes sense because I built this synthetic data from three sources. PCA is fast, it's a one-liner, and it's almost always the first thing I try on a new hyperspectral dataset. Notebook 01.

## Slide 15 — Clustering  
*(1:15)*

Closely related is clustering — automatically grouping similar pixels to produce phase or domain maps with no labels at all. The middle panel is the ground truth; the right panel is what KMeans recovers just from the data — and it's essentially right. One practical tip baked into this example: run PCA first to reduce the dimensionality, then cluster. It's faster and the clusters come out cleaner. And if you want to actually visualize how your spectra group, methods like t-SNE and UMAP project high-dimensional data down to a 2D scatter you can eyeball — that's in the optional notebook 08. This phase-mapping example is notebook 02.

## Slide 16 — PART 4 divider — Measuring smarter  
*(0:15)*

So far we've analyzed data after the fact. Part four flips that — using ML to change how we measure in the first place. Measuring smarter.

## Slide 17 — Sparse sampling  
*(1:15)*

Here's the core problem with SPM: it's slow. Every pixel costs you time, and a full high-resolution scan can take minutes the sample may not survive. So the question becomes: do we actually need every pixel? The answer is usually no. On this slide I measure only about ten percent of the pixels — chosen sparsely — and then reconstruct the full image with interpolation. Look at the error map on the right: it's tiny. Ninety percent fewer measurements, almost no loss. And the smarter move is to not sample randomly but to put your points where they matter — concentrate on edges and features, not flat regions. That idea — being deliberate about where you measure — leads straight into the next slide. This is notebook 03.

## Slide 18 — Autonomous SPM  
*(1:30)*

If you take sparse sampling to its logical conclusion, you get autonomous, self-driving microscopy. The instrument runs a closed loop: it measures a few points, builds a quick estimate of the surface, decides where the most informative next measurement is, goes there, and repeats — no human in the loop. The brain of this is the acquisition function, which balances two things: where am I most uncertain, and where is the surface most interesting or feature-rich. The payoff is on the right: the adaptive loop, in green, drives error down with far fewer measurements than random sampling in orange. This isn't science fiction — it's running on real instruments now, and notebook 04 gives you a complete, transparent toy implementation you can read end to end.

## Slide 19 — Annexin V HS-AFM — real data  
*(1:30)*

Let me show you all of this on real data, not synthetic. This is high-speed AFM of Annexin V proteins self-assembling on a lipid bilayer — about a hundred frames of a living, moving molecular process. On the left, a single raw frame; you can already see the ordered molecular lattice. The middle image is a dynamics map — the temporal standard deviation across all frames — and it instantly highlights where the action is, where the structure is changing. And on the right is a kymograph, a space-time slice, which reveals the assembly front advancing over time. Every technique from this talk — PCA denoising, clustering, dynamics analysis — comes together in this one real dataset, and it's all in the annexin notebook in the repo for you to explore.

## Slide 20 — PART 5 divider — The frontier  
*(0:15)*

Last part, and the fun one. Part five: the frontier — large language models, generative AI, and agents.

## Slide 21 — LLMs as a copilot  
*(1:15)*

Let's talk about large language models, because they're changing day-to-day work fast. Think of an LLM as a copilot for your microscope. First, as an analysis copilot: you describe in plain English what you want to do, and it writes and explains the analysis code — lowering the barrier to exactly the kind of notebooks I've been showing. Second, for literature and metadata: mining papers, pulling parameters out of old experiments, searching and summarizing your own pile of data. And third, foundation models — large pretrained models for images or spectra that you can fine-tune for an SPM task with surprisingly little labeled data. One honest reality check, though: LLMs accelerate the work around your science; they don't replace physical understanding, and they can be confidently wrong. Keep an expert — you — in the loop.

## Slide 22 — Generative AI & agents  
*(1:15)*

Two more frontier ideas. Generative AI — the same family as the image generators you've heard about — has real microscopy uses: diffusion models that denoise or super-resolve fast, noisy scans; generating synthetic data to train other models; and inverse design, where you specify the property you want and ask the model for a structure that delivers it. And then agents, which tie it all together. An agent plans, acts, observes, and decides — and notice that the autonomous microscopy from part four is an early, narrow example of exactly this. The vision is the self-driving lab: an agent that you give a goal and safety limits to, and it orchestrates the instrument, the database, and the analysis to chase that goal. You set the objective and the guardrails; it handles the busywork. We're early, but it's moving quickly.

## Slide 23 — Toolchain  
*(1:00)*

Quick practical note: none of this requires expensive software. Your entire stack is open-source, well-documented, and free. NumPy and SciPy for the array math and signal processing. Scikit-learn for classical ML — it's where you should start. PyTorch when you genuinely need deep learning. Matplotlib for visualization. Libraries like igor2 and h5py to read your SPM file formats. And Jupyter to tie it together interactively — which is where all of today's examples live. Importantly, the supervised notebooks, 05 through 07, need nothing more than scikit-learn, so there's no heavyweight setup standing between you and your first model.

## Slide 24 — Get the code  
*(1:00)*

So how do you actually get started? Two ways, and the QR code does both. If you want to run it: click 'Open in Colab' and it clones the repo and runs everything on a free cloud machine — nothing to install — or clone it locally with conda or pip. And if you just want to read along on your phone right now: every notebook is pre-run with all the figures saved inside, so the nbviewer links render fully with nothing to install. There are eight core notebooks, three optional ones, and the real-data HS-AFM case study. Scan the code, and it's all yours.

## Slide 25 — Common pitfalls  
*(1:00)*

Before I wrap, a few hard-won pitfalls, because you'll hit these. One: training on all your data — always hold out a test set first and don't touch it until the end. Two: ignoring class imbalance — if crashes are one percent of your scans, use stratified splits or class weights, or your model will just ignore them. Three: applying a model trained on one tip or sample to a totally different one — validate on the new conditions, and re-train when things shift. And four, which I've said before and will say again: don't report accuracy alone on imbalanced data — use precision, recall, and the confusion matrix. None of these are exotic; they're just discipline.

## Slide 26 — Realistic expectations  
*(1:00)*

And to keep expectations calibrated: ML is a tool, not a magic wand. It's genuinely great at repetitive tasks at scale, at labeling things consistently where humans drift, at pulling features out of noisy multi-channel data, at exploratory clustering, and at fast triage for anomalies. It struggles with very small labeled datasets, with wildly variable tip or sample conditions, with extrapolating outside what it was trained on, with giving you physical interpretation of its own predictions, and — crucially — it won't design your experiment for you. Use it for what it's good at, and keep your physics where it belongs: in your head.

## Slide 27 — Conclusion — Start today  
*(0:45)*

So here's my ask. You now have the concepts, the code, and hopefully the confidence. Don't let this be a talk you nod along to and forget. Clone the repo, open notebook 00, and run it on your own data — today, while it's fresh. The QR code is right here. I'd genuinely love to see what you do with it, so come find me afterward — questions, collaborations, war stories, all welcome. Thank you.
