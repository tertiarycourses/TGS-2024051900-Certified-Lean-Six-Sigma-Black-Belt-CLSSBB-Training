<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 18

## Multiple Regression and Model Diagnostics (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Build and validate a multiple regression model of your capstone Y (A3, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-18-multiple-regression.xlsx`**

Full model R-sq ~ 0.83, adjusted R-sq ~ 0.82. Significant: ClampPressure (b ~ +2.05 kPa/bar, p<0.001), DwellTime (b ~ +21.4 kPa/s, p<0.001), ElectrodeTipAge (b ~ -0.012 kPa/stroke, p<0.001). AmbientTemp and Humidity are NOT significant and have VIF > 10 — they are collinear (r ~ 0.75); drop one. The reduced 3-X model has essentially the same adjusted R-sq with a cleaner residual plot. Residuals are normal and show no pattern vs fits, so the model assumptions hold. Y = f(clamp, dwell, tip age) is the transfer function you optimise in the DOE.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your final model has all VIFs under 5, residual plots show no pattern, adjusted R-squared is reported, the model has been validated on held-out data, and each coefficient is stated in business terms.

## Where this sits in the capstone

BLACK BELT ONLY — the Green Belt course teaches simple linear regression with one X. Real processes have several interacting Xs. Multiple regression models them together, but a model that fits is not yet a model that is valid, so the diagnostics matter as much as the coefficients. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
