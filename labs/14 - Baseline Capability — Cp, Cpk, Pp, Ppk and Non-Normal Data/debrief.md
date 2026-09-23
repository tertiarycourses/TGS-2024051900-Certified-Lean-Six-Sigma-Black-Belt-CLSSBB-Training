<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 14

## Baseline Capability — Cp, Cpk, Pp, Ppk and Non-Normal Data

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Establish baseline capability for your capstone, handling non-normal data correctly (A4, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-14-baseline-capability.xlsx`**

BurstPressure: mean ~214.0, overall SD ~21.5. Pp = (260-180)/(6x21.5) = 0.62; Ppk = min(260-214, 214-180)/(3x21.5) = 0.53. Cpk (within) is slightly higher than Ppk, which tells you the process is not stable over time. Roughly 5.6% of units fall outside spec — about 2.9 sigma. THIS IS THE BASELINE the whole project improves; Lab 27 re-measures it at Ppk ~1.40. CycleTime is lognormal (Anderson-Darling p<0.005): do NOT compute Ppk on the raw data — transform (Box-Cox, lambda~0) or fit a lognormal distribution first.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

You have confirmed stability before computing capability, tested and documented normality with a p-value, handled non-normality by transformation or distribution fitting, and reported both Cpk and Ppk with an explanation of the gap.

## Where this sits in the capstone

Re-derive capability analysis in full, then go beyond Green Belt: the distinction between Cpk and Ppk that most practitioners get wrong, and what to do when the data is not normal — which is most of the time in cycle-time and defect data. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
