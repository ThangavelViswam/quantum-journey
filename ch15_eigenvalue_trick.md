# Chapter 15: A Quick Trick for Computing Eigenvalues

## Core Idea
- For 2×2 matrices, you can compute eigenvalues **in your head** using two facts:
  - The **mean** of the two eigenvalues = mean of the diagonal
  - The **product** of the two eigenvalues = determinant
- From mean m and product p:
  **λ = m ± √(m² − p)**

## Why It Works
- **Trace** of a matrix = sum of diagonal entries = sum of eigenvalues
  → mean of eigenvalues = trace / 2 = mean of diagonal
- **Determinant** = product of eigenvalues
  (det squishes/stretches area by the same factor the eigenvalues do, multiplied)
- Two numbers (sum, product) uniquely determine the two roots of a quadratic —
  that's all the characteristic polynomial λ² − (trace)λ + det = 0 ever needed
- Completing the square on that quadratic gives the m ± √(m² − p) form directly

## Worked Examples
- A = [[8, 4], [2, 6]]
  - m = (8 + 6) / 2 = 7
  - p = 8·6 − 4·2 = 40
  - λ = 7 ± √(49 − 40) = 7 ± 3 → **λ = 10, 4**
- A = [[3, 1], [4, 1]]
  - m = 2, p = 3 − 4 = −1
  - λ = 2 ± √(4 + 1) = 2 ± √5

## What the Discriminant Tells You
- **m² − p > 0**: two distinct real eigenvalues (stretch + stretch)
- **m² − p = 0**: repeated eigenvalue (shear-like; possibly defective)
- **m² − p < 0**: complex conjugate pair → rotational component, no real eigenvectors

## Why This Matters
- Skips the "set up characteristic polynomial, expand, factor" ritual entirely
- Builds intuition: every 2×2 transformation's spectrum is captured by just
  **trace and determinant** — its "average stretch" and "total area scaling"
- Generalizes: for n×n, the characteristic polynomial's coefficients are still
  symmetric functions of the eigenvalues (trace, det, and friends)

## Connections to Prior Chapters
- Ch 6 (Determinant): det = product of eigenvalues — area scaling factored
- Ch 14 (Eigenvectors & Eigenvalues): this is the shortcut for the same equation
- Ch 13 (Change of Basis): trace and det are **basis-invariant** — that's why
  this trick works regardless of how the matrix is written

## Quantum Computing Connection
- **2×2 matrices are the workhorse of single-qubit gates** — Pauli X/Y/Z, Hadamard,
  phase gates all live here, so this trick lets you read off eigenstructure by inspection
- For a Hermitian H = [[a, b], [b̄, d]], eigenvalues = m ± √(m² − p) gives you
  **measurement outcomes** directly — no diagonalization needed
- Trace and determinant of the density matrix ρ encode **purity** (Tr(ρ²)) and
  normalization (Tr(ρ) = 1) — same invariants, different role
- For a unitary U, |det(U)| = 1 and trace controls the **rotation angle** on the
  Bloch sphere: Tr(U) = 2cos(θ/2) for SU(2) rotations
