<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 15

## Variation, Run Charts, Pareto and Stratification — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Separate common from special cause variation and stratify your capstone data (A3).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-15-run-chart-pareto-stratification.xlsx`**

RunChart: the median is ~208 kPa. A clear SHIFT — the longest run below the median is 12 consecutive points, well past the 8-point rule, starting at day 38 when the new fixture batch was installed. The mean drops from ~215.5 to ~198.4 kPa. That is a special cause, not noise; do not tamper — investigate the fixture change. Pareto: 'Seal weld leak' (412) + 'Occlusion sensor drift' (168) = 69% of all 840 defects — the vital few. Stratification: Suzhou shift C runs ~3x the defect rate of every other cell. The problem is not 'the process', it is a specific plant-shift combination.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your run chart is assessed against all six patterns, your Pareto is weighted appropriately, and stratification has produced at least three named candidate Xs for statistical testing.

## Where this sits in the capstone

A full re-derivation of the foundation of all Six Sigma analysis: the distinction between common and special cause variation. Acting on common cause as if it were special (tampering) makes processes worse — this is the single most expensive mistake in process management. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
