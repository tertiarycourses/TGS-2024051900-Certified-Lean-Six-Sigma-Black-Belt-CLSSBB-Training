<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 11

## Continuous Gage R&R — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Validate a continuous measurement system for your capstone using Gage R&R (A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-11-gage-rr-continuous.xlsx`**

%Study Variation for Total Gage R&R lands around 38-42% (>30% = UNACCEPTABLE) and the number of distinct categories is 3 (<5 = inadequate). Reproducibility is the larger share: N. Faridah reads ~5.9 kPa high relative to T. Chandra. Fix the operator method (a written test procedure and re-training) before re-running the study; do NOT analyse baseline capability on this measurement system.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your study uses parts spanning the full process range with randomised blinded order, and you have computed %study variation and ndc with a stated accept/reject decision.

## Where this sits in the capstone

A full re-derivation of measurement system analysis for continuous data. Before any of the statistics in Days 3 and 4 can be trusted, the measurement system must be proven — an invalid gauge invalidates every conclusion that follows. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
