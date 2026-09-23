<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 24

## Fractional Factorial Designs, Confounding and Resolution (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Screen many factors efficiently and interpret confounded effects correctly (A3, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-24-fractional-factorial-doe.xlsx`**

Design generator E = ABCD, defining relation I = ABCDE, so this is RESOLUTION V: main effects are aliased with 4-factor interactions and 2-factor interactions with 3-factor interactions — both negligible, so every main effect and every 2-factor interaction is cleanly estimable. Significant: ClampPressure (+18.8), DwellTime (+14.2), ElectrodeTipAge (+9.2, i.e. a WORN tip costs ~9 kPa), and the clamp x dwell interaction (+11.6). AmbientTemp and SealRingSupplier are not significant. Half the runs, the same conclusions as Lab 23 — that is the point of fractionating.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

You stated the design resolution before running, wrote out the complete alias structure, and any ambiguous conclusion is either declared explicitly or resolved by a fold-over.

## Where this sits in the capstone

BLACK BELT ONLY. A full factorial on 7 factors needs 128 runs — usually unaffordable. Fractional factorials screen many factors in a fraction of the runs by deliberately trading away the ability to separate certain effects. The critical skill is knowing exactly WHAT you traded away, which is what resolution tells you. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
