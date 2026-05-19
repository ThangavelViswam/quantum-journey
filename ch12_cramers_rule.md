# Chapter 12: Cramer's Rule, Explained Geometrically

## Core Idea
- A method for solving **Ax = b** when det(A) ≠ 0
- Each coordinate of x is a **ratio of two determinants**:
  x_i = det(A_i) / det(A)
- A_i is A with its **i-th column replaced by b**

## The Geometric Trick
- The unknown vector x has coordinates (x, y) in the standard basis
- Look at the parallelogram formed by **î and x** — its signed area = y
  (because x stretches the j-direction by exactly y)
- Apply the transformation A — area scales by det(A), and î becomes the first column of A
- So the new parallelogram is spanned by **(col 1 of A)** and **A·x = b**
- Its signed area = y · det(A) = det([col 1 of A, b])
- Solve for y → that's Cramer's rule

## Why It Works
- Linear transformations scale **all** signed areas by det(A)
- Each coordinate of x can be read as a signed area in the input space
- After applying A, that same area shows up in the output space as a determinant we *can* compute
- The "replace a column with b" trick is just geometry: the column you replace is the one your unknown coordinate was measuring against

## Practical Notes
- Elegant but **computationally expensive** for large systems
  (Gaussian elimination wins in practice)
- Real value is conceptual: ties together determinants, linear systems, and geometry
- Only works when det(A) ≠ 0 → square, invertible systems

## Connections to Prior Chapters
- Ch 5–6 (Transformations & Determinant): area scaling is the whole engine
- Ch 7 (Inverse Matrices): alternative way to express x = A⁻¹b
- Ch 9 (Duality): coordinates as "measurements" against basis vectors

## Quantum Computing Connection
- Solving linear systems is the heart of **HHL algorithm** (Harrow-Hassidim-Lloyd) —
  exponential speedup for Ax = b on a quantum computer
- Determinant ratios appear in **amplitude amplification** and Grover-style problems
- Geometric view of "coordinates as signed areas" generalizes to **measurement
  probabilities** in Hilbert space — |⟨φ|ψ⟩|² is the projective analogue
