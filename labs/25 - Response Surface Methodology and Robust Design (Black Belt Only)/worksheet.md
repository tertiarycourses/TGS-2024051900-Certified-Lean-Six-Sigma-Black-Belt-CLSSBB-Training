<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Team Worksheet — Lab 25

## Response Surface Methodology and Robust Design (Black Belt Only)

**Team members:** ____________________________________________  
**Date:** ____________________

---

### 1. Our understanding of the problem

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 2. Our working

*Use the data in `lab-25-rsm-central-composite.xlsx`.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 3. What we produced

*Deliverable: An RSM study locating optimal settings plus a robust design analysis against noise factors.*

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

**Step 1.** Understand the limitation of 2-level designs: with only two levels per factor they fit a straight line and cannot detect curvature at all.

____________________________________________________________________________________

**Step 2.** Add CENTRE POINTS to your factorial design to test for curvature. A significant centre-point effect means the true response is curved and a linear model will mislead you.

____________________________________________________________________________________

**Step 3.** If no curvature is present and you are far from the optimum, use steepest ascent — move the factor settings in the direction of greatest improvement and re-experiment.

____________________________________________________________________________________

**Step 4.** Once curvature appears, you are near the optimum and need a second-order design.

____________________________________________________________________________________

**Step 5.** Learn the central composite design (CCD): a factorial core, plus centre points, plus axial (star) points that add the third level needed to estimate quadratic terms.

____________________________________________________________________________________

**Step 6.** Learn the Box-Behnken alternative: fewer runs than CCD and it never requires extreme corner combinations, which matters when corners are unsafe or infeasible.

____________________________________________________________________________________

**Step 7.** Design and run an RSM study on the 2-3 vital factors from Lab 24.

____________________________________________________________________________________

**Step 8.** Fit the second-order model including linear, quadratic and interaction terms.

____________________________________________________________________________________

**Step 9.** Generate contour and 3D surface plots to visualise the response surface and locate the optimum region.

____________________________________________________________________________________

**Step 10.** Find the stationary point and classify it — maximum, minimum or saddle. A saddle point means the optimum lies at a boundary, not in the middle.

____________________________________________________________________________________

**Step 11.** Use desirability functions if you must optimise several responses at once with competing optima.

____________________________________________________________________________________

**Step 12.** Now robust design. Separate your factors into CONTROL factors (you set them) and NOISE factors (ambient conditions, material variation, operator, wear).

____________________________________________________________________________________

**Step 13.** Understand the Taguchi insight: choose control factor settings at which the response is LEAST SENSITIVE to noise — a slightly lower mean with far less variation usually wins.

____________________________________________________________________________________

**Step 14.** Compute the signal-to-noise ratio for candidate settings, using the correct form for your objective (smaller-is-better, larger-is-better or nominal-is-best).

____________________________________________________________________________________

**Step 15.** Select the robust operating window and run confirmation trials under deliberately varied noise conditions.

____________________________________________________________________________________

### 7. Self-check

Curvature is tested with centre points, your second-order model is visualised as a contour or surface plot with a classified stationary point, and the robust settings are confirmed under varied noise conditions.

Complete?  ☐ Yes   ☐ Not yet

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
