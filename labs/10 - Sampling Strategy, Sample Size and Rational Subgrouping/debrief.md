<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 10

## Sampling Strategy, Sample Size and Rational Subgrouping

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Determine defensible sample sizes and design rational subgroups for your capstone (A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-10-sampling-frame.xlsx`**

The population mean is ~214 kPa with SD ~21.5. A simple random sample of n=30 estimates the mean well but hides the plant-to-plant difference; a sample stratified by plant exposes it. For a margin of error of 5 kPa at 95% confidence, n = (1.96 x 21.5 / 5)^2 ~ 71 units.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your sample sizes are calculated from a real estimate of s or p, your subgrouping scheme places common-cause variation within subgroups, and you can state the shift size your plan can detect.

## Where this sits in the capstone

Re-derive sampling schemes and sample size formulas in full, then go beyond Green Belt with RATIONAL SUBGROUPING — the decision that silently determines what your control charts in Day 4 will be capable of detecting at all. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

## The running process — figures that must reconcile

| Checkpoint | Value | Established in |
|---|---|---|
| Baseline defect rate | 2.9% | Lab 3 |
| Measurement system | FAILS Gage R&R (~40% study variation) | Lab 11 |
| Baseline capability | Pp 0.62 / Ppk 0.53 | Lab 14 |
| Proven Xs | clamp pressure, dwell time, electrode tip age | Labs 18-21 |
| DOE optimum | clamp 47.4 bar, dwell 2.76 s | Labs 23-25 |
| Improved capability | Ppk 1.40 | Lab 27 |
| Annual hard benefit | SGD 487,000 vs SGD 812,000 COPQ | Labs 1, 30 |

If a learner's number disagrees with the column above, they have either used their own workplace data (fine — say so) or made an error (find it).

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd · TRAINER ONLY*
