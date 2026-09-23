<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 25

## Response Surface Methodology and Robust Design (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Optimise factor settings using RSM and make the process robust to noise (A5, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-25-rsm-central-composite.xlsx`**

The 5 centre points reveal significant CURVATURE (p<0.001) — a first-order model is inadequate, which is exactly why you escalate from factorial to RSM. Fitted second-order model R-sq ~ 0.96 with significant negative quadratic terms in both factors, so the surface is a dome with an interior MAXIMUM. Stationary point: clamp ~ 47.4 bar, dwell ~ 2.76 s, predicted Y ~ 242.5 kPa. Robustness: the surface is flat near the peak, so a +/-1 bar drift costs under 1 kPa — the setting is robust to normal process noise. These are the settings the Lab 26 pilot runs and the Lab 27 control plan holds.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Curvature is tested with centre points, your second-order model is visualised as a contour or surface plot with a classified stationary point, and the robust settings are confirmed under varied noise conditions.

## Where this sits in the capstone

BLACK BELT ONLY. Factorial designs find WHICH factors matter; RSM finds the OPTIMUM SETTINGS by modelling curvature that a two-level design cannot see. Taguchi robust design then goes further — setting the process so it performs consistently despite noise you cannot control. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
