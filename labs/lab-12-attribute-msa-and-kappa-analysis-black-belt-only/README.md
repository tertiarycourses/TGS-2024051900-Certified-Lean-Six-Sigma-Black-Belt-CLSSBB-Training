# Lab 12 — Attribute MSA and Kappa Analysis (Black Belt Only)

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Validate a judgement-based measurement system using attribute agreement and Kappa (A4, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

An attribute agreement study with within-, between- and versus-standard Kappa values.

**Tools and techniques:** Attribute agreement analysis, Cohen's Kappa, Fleiss' Kappa, within/between appraiser agreement, agreement vs standard

## Data files in this folder

- **`lab-12-attribute-msa-kappa.xlsx`** — *Dataset.* Attribute agreement study — 50 seal-weld photos, 3 inspectors, 2 trials each, against a known expert reference standard.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Establish why Gage R&R fails for attribute data: there is no continuous scale on which to compute variance components.

### Step 2

Identify a judgement-based measurement in your capstone — visual inspection, cosmetic grading, document approval, claim adjudication or defect classification.

### Step 3

Select 30 to 50 sample items spanning clear-pass, clear-fail and deliberately borderline cases. Borderline items are where agreement actually breaks down.

### Step 4

Have an expert establish the KNOWN STANDARD (true) classification for every item. Without a standard you can measure consistency but never correctness.

### Step 5

Have 3 appraisers each classify every item twice, in randomised order, blinded to their own previous answer and to each other.

### Step 6

Calculate WITHIN-appraiser agreement — does each inspector agree with themselves? Self-disagreement is the most common and most ignored failure.

### Step 7

Calculate BETWEEN-appraiser agreement — do the inspectors agree with each other?

### Step 8

Calculate agreement VERSUS THE STANDARD — are they collectively correct, or consistently wrong together?

### Step 9

Compute Cohen's Kappa for appraiser pairs and Fleiss' Kappa across all appraisers. Kappa corrects raw agreement for agreement expected by chance.

### Step 10

Apply the acceptance rule: Kappa >= 0.90 excellent, 0.75-0.90 acceptable, below 0.75 requires action. Note that 90% raw agreement can still yield a poor Kappa.

### Step 11

Where agreement fails, prescribe the fix: boundary samples, photographic standards, tightened operational definitions or appraiser retraining. Then re-run.

## Check your work

Your study includes borderline items and a known standard, you have computed within-appraiser, between-appraiser and versus-standard agreement plus Kappa, and you have an action plan for any Kappa below 0.75.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
