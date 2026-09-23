<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 19

## ANOVA, Interactions and Non-Parametric Tests (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Compare multiple groups using ANOVA and apply non-parametric alternatives (A3, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-19-anova-interactions-nonparametric.xlsx`**

OneWay: means are A 224.8, B 226.2, C 204.3, D 221.8. F ~ 14, p < 0.001 — at least one supplier differs. Tukey shows Supplier C is significantly lower than A, B and D (which do not differ from each other). Act on Supplier C, not on 'suppliers' in general. TwoWay: Plant p<0.001, Shift p~0.03, and the Plant x Shift INTERACTION p<0.001. Because the interaction is significant you must NOT interpret the main effects alone — Suzhou shift C is the specific bad cell, matching Labs 15 and 17. NonParametric: the data are strongly right-skewed, so ANOVA is invalid; Kruskal-Wallis H ~ 24.6, p < 0.001 — Line 3 cycle times are significantly higher.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your ANOVA assumptions are tested and documented, significant results carry a post-hoc analysis, you have interpreted an interaction plot, and at least one finding is confirmed non-parametrically.

## Where this sits in the capstone

BLACK BELT ONLY. Comparing three or more groups with repeated t-tests inflates the false-positive rate badly — ANOVA solves this. Two-way ANOVA then reveals interaction effects that one-factor analysis cannot see. And when normality fails, non-parametric tests are the correct answer rather than proceeding regardless. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
