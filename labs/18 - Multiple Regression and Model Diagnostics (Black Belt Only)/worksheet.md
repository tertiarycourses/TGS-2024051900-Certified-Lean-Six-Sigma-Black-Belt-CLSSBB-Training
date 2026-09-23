<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Team Worksheet — Lab 18

## Multiple Regression and Model Diagnostics (Black Belt Only)

**Team members:** ____________________________________________  
**Date:** ____________________

---

### 1. Our understanding of the problem

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 2. Our working

*Use the data in `lab-18-multiple-regression.xlsx`.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 3. What we produced

*Deliverable: A validated multiple regression model with full residual and multicollinearity diagnostics.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 4. What the evidence does NOT tell us

____________________________________________________________________________________

____________________________________________________________________________________

### 5. Our conclusion

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 6. Step notes

**Step 1.** Recap simple linear regression: the fitted line, slope interpretation, R-squared and the correlation-is-not-causation trap.

____________________________________________________________________________________

**Step 2.** Extend to multiple regression: Y = b0 + b1X1 + b2X2 + ... + e, where each coefficient is the effect of that X holding all other Xs constant.

____________________________________________________________________________________

**Step 3.** Understand why that 'holding constant' clause matters — it is what makes multiple regression fundamentally different from running several simple regressions.

____________________________________________________________________________________

**Step 4.** Assemble your capstone dataset with the Y and at least four candidate Xs, with enough rows (a common rule of thumb is 10-15 observations per X).

____________________________________________________________________________________

**Step 5.** Fit the full model and record the coefficients, their p-values, R-squared and adjusted R-squared.

____________________________________________________________________________________

**Step 6.** Use ADJUSTED R-squared, not R-squared, to compare models. Plain R-squared always rises when you add an X, even a random one.

____________________________________________________________________________________

**Step 7.** Check multicollinearity with Variance Inflation Factors. VIF > 5 is a concern, VIF > 10 is serious — correlated Xs make coefficients unstable and signs nonsensical.

____________________________________________________________________________________

**Step 8.** Resolve multicollinearity by dropping or combining redundant Xs, then refit.

____________________________________________________________________________________

**Step 9.** Run the residual diagnostics in full: residuals versus fitted values (should show no pattern), normal probability plot of residuals, and residuals versus order (independence).

____________________________________________________________________________________

**Step 10.** Interpret residual patterns: a funnel shape indicates non-constant variance, curvature indicates a missing quadratic term, and drift over order indicates autocorrelation.

____________________________________________________________________________________

**Step 11.** Reduce to the final model using backward elimination — drop the least significant X, refit, and repeat until all remaining Xs are significant.

____________________________________________________________________________________

**Step 12.** Guard against overfitting: hold back a validation subset, or use cross-validation, and confirm the model predicts data it has not seen.

____________________________________________________________________________________

**Step 13.** Translate the final model into business language: for each significant X, state what a one-unit change does to Y in customer or dollar terms.

____________________________________________________________________________________

### 7. Self-check

Your final model has all VIFs under 5, residual plots show no pattern, adjusted R-squared is reported, the model has been validated on held-out data, and each coefficient is stated in business terms.

Complete?  ☐ Yes   ☐ Not yet

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
