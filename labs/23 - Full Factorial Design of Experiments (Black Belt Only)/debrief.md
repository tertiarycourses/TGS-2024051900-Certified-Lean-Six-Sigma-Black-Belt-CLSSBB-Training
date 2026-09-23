<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 23

## Full Factorial Design of Experiments (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Design, run and analyse a full factorial experiment on your capstone process (A3, A5, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-23-full-factorial-doe.xlsx`**

Main effects: ClampPressure +18.8 kPa (p<0.001), DwellTime +14.2 kPa (p<0.001), AmbientTemp -4.0 kPa (not significant, p~0.09). The AB (clamp x dwell) INTERACTION is +11.6 kPa and highly significant (p<0.001) — this is why one-factor-at-a-time would have missed the optimum. R-sq ~ 0.97. Best setting: clamp HIGH (46 bar) and dwell HIGH (2.7 s), predicted Y ~ 240 kPa, comfortably centred in the 180-260 spec. Temperature can be left uncontrolled. Carry these settings into Labs 24-25.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your design is fully randomised with replication, you have computed and plotted both main effects and interactions, effect significance is assessed statistically, and confirmation runs validate the predicted optimum.

## Where this sits in the capstone

BLACK BELT ONLY — the Green Belt course mentions DOE in passing; the Black Belt owns it. One-factor-at-a-time experimentation is slower, less informative and structurally incapable of detecting interactions. Full factorial designs estimate every main effect AND every interaction. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
