<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 13

## Nested and Destructive Gauge Studies (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Design a valid MSA when parts cannot be measured repeatedly (A4, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-13-nested-destructive-gauge.xlsx`**

A crossed Gage R&R is impossible here: the test destroys the part, so no operator can repeat another's measurement. Use a NESTED design and treat within-batch specimen variation as the repeatability estimate — valid only if the batch is homogeneous. Nested ANOVA gives measurement variation ~21% of study variation (marginal); batch-to-batch dominates, which is what you want.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

You can explain why a crossed study is invalid for your measurement, your batches are justified as homogeneous, and your report states the repeatability/part-variation confounding explicitly.

## Where this sits in the capstone

BLACK BELT ONLY. The crossed Gage R&R of Lab 11 assumes every operator can measure every part repeatedly. Destructive tests (tensile, burst, seal strength, chemical assay) break that assumption entirely — measuring consumes the part. The nested design is the correct answer, and using a crossed study here produces confident nonsense. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
