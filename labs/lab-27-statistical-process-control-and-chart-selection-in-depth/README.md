# Lab 27 — Statistical Process Control and Chart Selection — In Depth

**DMAIC phase:** CONTROL  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Select and construct the correct control chart for your capstone Y (A5, K1).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

A correctly selected and constructed control chart for your capstone Y with applied run rules.

**Tools and techniques:** Chart anatomy, control limits, Xbar-R, Xbar-S, I-MR, p, np, c, u charts, Western Electric rules, control vs spec limits

## Data files in this folder

- **`lab-27-spc-control-charts.xlsx`** — *Dataset.* Post-improvement control data: 30 subgroups of 5 for an Xbar-R chart, 40 individual clamp-pressure readings for an I-MR chart, and 24 weeks of defective counts for a p chart.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Recap SPC purpose in full: distinguish signal from noise over time, so drift is caught before it becomes a defect.

### Step 2

Recap chart anatomy: centre line, upper and lower control limits at +/- 3 sigma, and why 3 sigma balances false alarms against missed signals.

### Step 3

Establish the critical distinction: CONTROL limits come from the process's own voice (the data); SPECIFICATION limits come from the customer. They are unrelated and must never be drawn on the same axis as if comparable.

### Step 4

Learn the chart selection logic in full. Continuous data: subgroup size 1 = I-MR; 2-8 = Xbar-R; 9+ = Xbar-S.

### Step 5

Learn the attribute branch: defectives with constant sample size = np; varying = p. Defects with constant opportunity = c; varying = u.

### Step 6

Select the correct chart for your capstone Y and write down the justification. Selecting the wrong chart produces wrong limits and false confidence.

### Step 7

Collect at least 25 subgroups of baseline data — fewer gives control limits too unstable to be trustworthy.

### Step 8

Calculate the control limits using the correct constants (A2, D3, D4 for Xbar-R; equivalent constants for other charts).

### Step 9

Plot the chart and apply the Western Electric run rules in full: 1 point beyond 3 sigma; 2 of 3 beyond 2 sigma; 4 of 5 beyond 1 sigma; 8 consecutive on one side; trends; and hugging the centre line.

### Step 10

Investigate every signal. If a special cause is found and removed, recalculate the limits excluding that point — but only with a documented assignable cause.

### Step 11

Confirm the process is stable before proceeding. An unstable process has no meaningful capability and cannot be controlled by a control plan alone.

## Check your work

Your chart selection is justified against the selection logic, limits are computed from 25+ subgroups with the correct constants, and all run rules are applied with every signal investigated.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
