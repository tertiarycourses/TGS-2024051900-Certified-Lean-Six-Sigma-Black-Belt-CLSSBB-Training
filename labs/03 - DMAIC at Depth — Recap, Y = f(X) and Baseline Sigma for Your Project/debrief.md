<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 3

## DMAIC at Depth — Recap, Y = f(X) and Baseline Sigma for Your Project

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Re-derive the DMAIC roadmap and express your capstone as Y = f(X) with a baseline sigma level (K1, A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-03-baseline-sigma-calculator.xlsx`**

Full-year totals: 49,565 units, 1,742 defects, 1,442 defective units. DPU = 1742/49565 = 0.0351. DPO = 0.0351/4 = 0.00878. DPMO = 8,784. Yield (units with no defect) = 97.1%, so the defect rate is 2.9% — the baseline every later lab quotes. From the DPMO table that is about 3.9 sigma at the OPPORTUNITY level, but only ~2.9 sigma at the UNIT level; always state which one you mean. RTY = 0.980 x 0.971 x 0.991 x 0.996 x 0.971 x 0.997 = 0.909 — a 9.1% hidden factory that the final-yield number completely conceals. The seal weld and burst test steps are the two worst, which is exactly where the project is aimed.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

You can explain all five DMAIC tollgates without notes, your Y is a measurable customer-facing output with at least twelve classified Xs, and your baseline DPMO and sigma level are calculated from real counts.

## Where this sits in the capstone

A thorough recap of the DMAIC roadmap — not a skim, because you must be able to mentor Green Belts through it. Then apply it: express your capstone problem as Y = f(X), and convert your baseline defect data into DPMO and a sigma level so improvement can be proven numerically at the end. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
