<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 27

## Statistical Process Control and Chart Selection — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Select and construct the correct control chart for your capstone Y (A5, K1).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-27-spc-control-charts.xlsx`**

XbarR: chart the subgroup means. Centre line ~221 kPa, UCL ~233.5, LCL ~208.5. Subgroups 24 and 25 sit ABOVE the UCL — a genuine special cause (a fixture reset during that shift). Investigate and exclude before computing capability. With those points removed the process is stable: Ppk ~ 1.40, up from the 0.62 baseline in Lab 14. I-MR: clamp pressure is in control at ~47.4 bar (the Lab 25 optimum), so the control plan is holding the X. Use I-MR, not Xbar-R — these are individual readings with no rational subgroup. pChart: an obvious sustained step down at week 13 when the improvement went live — 2.9% to 1.2% defective. Recalculate the control limits AFTER week 13; carrying the old limits forward is a classic SPC error.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your chart selection is justified against the selection logic, limits are computed from 25+ subgroups with the correct constants, and all run rules are applied with every signal investigated.

## Where this sits in the capstone

A full re-derivation of SPC — chart anatomy, the selection logic, control limits and the out-of-control rules. You must be able to teach this to Green Belts and audit their chart choices, which is a core Black Belt accountability. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
