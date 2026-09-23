<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 18 — Multiple Regression and Model Diagnostics (Black Belt Only)

**ANALYZE** · Build and validate a multiple regression model of your capstone Y (A3, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | ANALYZE |
| Lab type | Core |
| Deliverable | A validated multiple regression model with full residual and multicollinearity diagnostics. |
| Tools | Multiple regression, coefficients, adjusted R-squared, residual analysis, multicollinearity/VIF, model selection, overfitting |
| Data file | `lab-18-multiple-regression.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-18-multiple-regression.xlsx`** — *Dataset.* 120 production runs with five candidate Xs against burst pressure — including two predictors that are collinear on purpose.

| Sheet | What it contains | Rows |
|---|---|---|
| RegressionData | One row per production run, all Xs measured at the time of the run. | 120 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Recap simple linear regression: the fitted line, slope interpretation, R-squared and the correlation-is-not-causation trap.
2. Extend to multiple regression: Y = b0 + b1X1 + b2X2 + ... + e, where each coefficient is the effect of that X holding all other Xs constant.
3. Understand why that 'holding constant' clause matters — it is what makes multiple regression fundamentally different from running several simple regressions.
4. Assemble your capstone dataset with the Y and at least four candidate Xs, with enough rows (a common rule of thumb is 10-15 observations per X).
5. Fit the full model and record the coefficients, their p-values, R-squared and adjusted R-squared.
6. Use ADJUSTED R-squared, not R-squared, to compare models. Plain R-squared always rises when you add an X, even a random one.
7. Check multicollinearity with Variance Inflation Factors. VIF > 5 is a concern, VIF > 10 is serious — correlated Xs make coefficients unstable and signs nonsensical.
8. Resolve multicollinearity by dropping or combining redundant Xs, then refit.
9. Run the residual diagnostics in full: residuals versus fitted values (should show no pattern), normal probability plot of residuals, and residuals versus order (independence).
10. Interpret residual patterns: a funnel shape indicates non-constant variance, curvature indicates a missing quadratic term, and drift over order indicates autocorrelation.
11. Reduce to the final model using backward elimination — drop the least significant X, refit, and repeat until all remaining Xs are significant.
12. Guard against overfitting: hold back a validation subset, or use cross-validation, and confirm the model predicts data it has not seen.
13. Translate the final model into business language: for each significant X, state what a one-unit change does to Y in customer or dollar terms.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your final model has all VIFs under 5, residual plots show no pattern, adjusted R-squared is reported, the model has been validated on held-out data, and each coefficient is stated in business terms.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-18-multiple-regression.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
