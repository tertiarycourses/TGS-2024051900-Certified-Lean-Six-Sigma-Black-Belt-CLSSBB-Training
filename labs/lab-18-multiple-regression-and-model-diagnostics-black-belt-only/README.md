# Lab 18 — Multiple Regression and Model Diagnostics (Black Belt Only)

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Build and validate a multiple regression model of your capstone Y (A3, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

A validated multiple regression model with full residual and multicollinearity diagnostics.

**Tools and techniques:** Multiple regression, coefficients, adjusted R-squared, residual analysis, multicollinearity/VIF, model selection, overfitting

## Data files in this folder

- **`lab-18-multiple-regression.xlsx`** — *Dataset.* 120 production runs with five candidate Xs against burst pressure — including two predictors that are collinear on purpose.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Recap simple linear regression: the fitted line, slope interpretation, R-squared and the correlation-is-not-causation trap.

### Step 2

Extend to multiple regression: Y = b0 + b1X1 + b2X2 + ... + e, where each coefficient is the effect of that X holding all other Xs constant.

### Step 3

Understand why that 'holding constant' clause matters — it is what makes multiple regression fundamentally different from running several simple regressions.

### Step 4

Assemble your capstone dataset with the Y and at least four candidate Xs, with enough rows (a common rule of thumb is 10-15 observations per X).

### Step 5

Fit the full model and record the coefficients, their p-values, R-squared and adjusted R-squared.

### Step 6

Use ADJUSTED R-squared, not R-squared, to compare models. Plain R-squared always rises when you add an X, even a random one.

### Step 7

Check multicollinearity with Variance Inflation Factors. VIF > 5 is a concern, VIF > 10 is serious — correlated Xs make coefficients unstable and signs nonsensical.

### Step 8

Resolve multicollinearity by dropping or combining redundant Xs, then refit.

### Step 9

Run the residual diagnostics in full: residuals versus fitted values (should show no pattern), normal probability plot of residuals, and residuals versus order (independence).

### Step 10

Interpret residual patterns: a funnel shape indicates non-constant variance, curvature indicates a missing quadratic term, and drift over order indicates autocorrelation.

### Step 11

Reduce to the final model using backward elimination — drop the least significant X, refit, and repeat until all remaining Xs are significant.

### Step 12

Guard against overfitting: hold back a validation subset, or use cross-validation, and confirm the model predicts data it has not seen.

### Step 13

Translate the final model into business language: for each significant X, state what a one-unit change does to Y in customer or dollar terms.

## Check your work

Your final model has all VIFs under 5, residual plots show no pattern, adjusted R-squared is reported, the model has been validated on held-out data, and each coefficient is stated in business terms.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
