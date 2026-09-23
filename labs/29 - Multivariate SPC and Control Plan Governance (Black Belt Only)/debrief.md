<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 29

## Multivariate SPC and Control Plan Governance (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Monitor correlated characteristics with Hotelling's T-squared and govern control plans (A5, K1).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-29-multivariate-spc-control-plan.xlsx`**

MultivariateData: clamp and dwell are strongly correlated (r ~ +0.88 overall, and ~+0.99 once the two out-of-control points are excluded) in normal operation. Charted SEPARATELY on two I-MR charts, every point looks in control. A Hotelling T-squared chart signals at observations 33 and 34, where the CORRELATION breaks even though each variable individually stays inside its own limits. That is the failure mode univariate SPC cannot see, and the reason multivariate SPC exists. ControlPlan: every reaction plan must name WHO acts, WHAT they do and what happens to product made since the last good check — a reaction plan that says only 'investigate' is not a control.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your correlated characteristics are confirmed by a correlation matrix before applying T-squared, every control plan metric has a specific named reaction plan, and you have defined an audit cadence with explicit criteria.

## Where this sits in the capstone

BLACK BELT ONLY. When several correlated characteristics matter, running separate charts inflates false alarms and — more dangerously — misses failures visible only in the correlation structure. Then step up to the portfolio view: the Black Belt audits control plans across projects, not just their own. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
