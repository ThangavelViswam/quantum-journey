# Chapter 14: Eigenvectors and Eigenvalues

## Core Idea
- Most vectors get knocked off their span by a linear transformation
- A few special ones **stay on their own span** — they only get stretched or squished
- Those vectors are **eigenvectors**; the stretch factor is the **eigenvalue**
- Negative eigenvalue → vector flips direction but stays on the same line

## The Defining Equation
- **A v = λ v**
  - A: the transformation (matrix)
  - v: the eigenvector (non-zero)
  - λ: the eigenvalue (scalar)
- Rewrite as **(A − λI) v = 0** — a non-zero v in the null space of (A − λI)
- That requires (A − λI) to **squish space** → **det(A − λI) = 0**
- Solving this characteristic equation gives the eigenvalues

## Finding Them
1. Write det(A − λI) = 0 → polynomial in λ
2. Roots are the eigenvalues
3. For each λ, solve (A − λI) v = 0 to get the eigenvectors

## Geometric Cases
- **Rotation (no real eigenvectors)**: every vector leaves its span → eigenvalues are
  complex (rotation lives in the complex plane)
- **Shear**: one eigenvalue λ = 1, one eigenvector line (î stays put)
- **Scaling**: every vector is an eigenvector, single eigenvalue
- **Repeated eigenvalue**: may or may not have a full plane of eigenvectors

## Eigenbasis
- A basis made entirely of eigenvectors
- In this basis, the transformation matrix is **diagonal** — eigenvalues on the diagonal
- Diagonal matrices are trivially easy: A^n just raises each diagonal entry to the n-th power
- To exploit this: **A = P D P⁻¹**, where P's columns are eigenvectors, D is diagonal
- This is the change-of-basis sandwich from Ch 13, applied to make life easy

## Why It Matters
- Reveals the **invariant directions** of a transformation — its skeleton
- Computing A^n, matrix exponentials, and dynamical systems all become trivial
  in an eigenbasis
- Not every matrix is diagonalizable (defective matrices) — but symmetric/Hermitian
  ones always are, with orthogonal eigenvectors

## Connections to Prior Chapters
- Ch 3 (Linear Transformations): eigenvectors are the directions the transformation respects
- Ch 6 (Determinant): det(A − λI) = 0 is "the transformation squishes space"
- Ch 7 (Inverse Matrices / Null Space): eigenvectors live in null(A − λI)
- Ch 13 (Change of Basis): diagonalization is the eigenbasis change of basis

## Quantum Computing Connection
- **Observables** in QM are Hermitian operators; their **eigenvalues are the possible
  measurement outcomes** and eigenvectors are the corresponding states
- Measuring an observable **collapses** the state onto one of its eigenvectors
- **Spectral decomposition**: H = Σ λ_i |v_i⟩⟨v_i| — the foundation of everything
  from energy levels to quantum gates
- **Time evolution** U = e^(−iHt/ħ) is trivial in the eigenbasis of H — just phases
  on each eigenvalue
- **Quantum Phase Estimation** (core of Shor's algorithm, HHL, quantum chemistry)
  is literally an algorithm for extracting eigenvalues of a unitary
