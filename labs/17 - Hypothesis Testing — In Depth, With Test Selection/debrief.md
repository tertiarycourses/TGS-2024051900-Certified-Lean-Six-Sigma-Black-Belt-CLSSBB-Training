<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 17

## Hypothesis Testing — In Depth, With Test Selection

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Test your capstone's candidate causes with correctly selected hypothesis tests (A3, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-17-hypothesis-testing.xlsx`**

TwoSample: t ~ -3.24, p ~ 0.002 — REJECT H0. The new fixture raises mean burst pressure by ~14.3 kPa. Check equal variances first (F-test p>0.05, so pooled t is fine). Paired: mean difference ~ +8.9 kPa, t ~ 8.0, p < 0.001 — REJECT H0. Re-training works. A 2-sample t here would be WRONG: the observations are paired by operator. TwoProportion: Suzhou 8.8% vs Singapore 3.1%, z ~ 7.1, p < 0.001 — REJECT H0. Confirms the Lab 15 stratification finding statistically.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Every test has a documented selection justification and assumption check, results report effect size alongside the p-value, and you maintain both a confirmed-cause and a rejected-cause log.

## Where this sits in the capstone

A full re-derivation of hypothesis testing, including the test selection logic that Green Belts most often get wrong. You must be able to choose the right test, defend the choice, and explain the result in business language. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
