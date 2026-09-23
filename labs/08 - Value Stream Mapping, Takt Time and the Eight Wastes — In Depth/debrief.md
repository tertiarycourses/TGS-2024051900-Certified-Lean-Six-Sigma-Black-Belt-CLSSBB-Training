<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 8

## Value Stream Mapping, Takt Time and the Eight Wastes — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Build a value stream map of your capstone process and quantify waste (A2, A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-08-value-stream-map.xlsx`**

Available time = 2 shifts x (480 - 45) min - 30 min = 840 min = 50,400 s/day. Demand = 4200/22 = 191 units/day. TAKT = 50,400/191 = 264 s/unit. Only ONE step exceeds takt: Burst test at 360 s — it is the bottleneck and it constrains the whole line. Seal weld at 180 s is well inside takt, so the seal weld problem is a QUALITY problem, not a speed problem; do not try to fix it with more capacity. Total WIP is 1,410 units against 191/day of demand = 7.4 days of inventory sitting between steps. Value-added time is 1,235 s out of a 7.4-day lead time — a process cycle efficiency near 0.2%, which is typical and always shocking the first time a team computes it. The dominant wastes are Waiting (queues after every handoff) and Defects (the 2.9% that flows to rework), and Defects is where the capstone project attacks.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your VSM shows both material and information flow, you have calculated the value-added ratio and takt time from real numbers, and every logged waste carries a time or dollar quantification.

## Where this sits in the capstone

A full re-derivation of value stream mapping — material AND information flow, value-added ratio, takt time and the eight wastes — then applied to your own capstone process to expose where lead time is actually consumed. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
