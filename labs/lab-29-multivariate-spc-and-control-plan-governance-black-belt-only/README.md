# Lab 29 — Multivariate SPC and Control Plan Governance (Black Belt Only)

**DMAIC phase:** CONTROL  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Monitor correlated characteristics with Hotelling's T-squared and govern control plans (A5, K1).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

A Hotelling T-squared chart plus a governed control plan for your capstone.

**Tools and techniques:** Multivariate SPC, Hotelling T-squared, correlation structure, false alarm inflation, control plan, response plan, audit cadence

## Data files in this folder

- **`lab-29-multivariate-spc-control-plan.xlsx`** — *Dataset.* 50 paired clamp/dwell readings where the two variables are normally correlated — plus the project's draft control plan to govern.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Understand the false alarm problem: 5 separate charts each at alpha = 0.0027 gives a combined false alarm rate over 1.3 percent — five times intended.

### Step 2

Understand the more serious failure: two characteristics can each sit within their own limits while their COMBINATION is impossible, and separate charts will never see it.

### Step 3

Identify a set of correlated characteristics in your capstone — dimensions on one part, or related cycle times across linked steps.

### Step 4

Compute the correlation matrix and confirm the characteristics are genuinely correlated. If they are independent, separate charts are fine.

### Step 5

Learn Hotelling's T-squared: it collapses several correlated characteristics into one statistic accounting for the covariance structure.

### Step 6

Build the T-squared chart with its upper control limit from the F-distribution, and note there is no lower limit — T-squared is always positive.

### Step 7

Understand the interpretation difficulty: a T-squared signal tells you something is wrong but not which variable. Use decomposition or individual charts as a follow-up diagnostic.

### Step 8

Now build your capstone control plan in full: for each critical X and the Y — the metric, target, specification, measurement method, sample size, frequency, chart type, owner and reaction plan.

### Step 9

Write the reaction plan for each metric as a specific instruction: containment action, escalation path, named owner and time limit. 'Investigate' is not a reaction plan.

### Step 10

Add the control plan to the process documentation and update the SOP, training material and visual management boards.

### Step 11

Step up to portfolio governance: as Black Belt you audit control plans across multiple projects. Define your audit cadence and criteria.

### Step 12

Define what a control plan audit checks: is the chart still being maintained, are signals being actioned, is the owner still in post, and has the process drifted since handover?

### Step 13

Identify the most common decay mode — charts maintained but signals never actioned — and write your countermeasure for it.

## Check your work

Your correlated characteristics are confirmed by a correlation matrix before applying T-squared, every control plan metric has a specific named reaction plan, and you have defined an audit cadence with explicit criteria.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
