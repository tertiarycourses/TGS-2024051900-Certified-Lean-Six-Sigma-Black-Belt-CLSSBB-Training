<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 20

## Multi-Vari Studies and Chi-Square Analysis (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Decompose variation by family using a multi-vari study and test categorical association (A3, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-20-multivari-chisquare.xlsx`**

MultiVari: the LINE-TO-LINE (cyclical) family dominates — L3 sits ~9 kPa below L1 and L2, while cavity-to-cavity (positional) spans only ~3 kPa and the time-to-time (temporal) drift is ~1 kPa across the shift. Focus the investigation on what is different about Line 3; stop sampling the other two families. ChiSquare: chi-sq ~ 21.3, df = 6, p < 0.01 — defect MODE is not independent of plant. Suzhou's excess is concentrated in seal weld leaks specifically, which points back at the fixture, not at a general quality problem.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your multi-vari chart captures all three families with quantified variance contributions, your cause list is re-prioritised against the dominant family, and your chi-square satisfies the expected-frequency condition.

## Where this sits in the capstone

BLACK BELT ONLY. Before spending money hunting a root cause, find out WHERE the variation actually lives. A multi-vari study separates positional, cyclical and temporal variation — and frequently reveals that the team has been investigating entirely the wrong family. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
