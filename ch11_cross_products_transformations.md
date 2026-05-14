# Chapter 11: Cross Products via Transformations

## Core Idea
- Re-derive the 3D cross product using **duality** (Ch 9 insight)
- Define a function f(v) = det of the 3×3 matrix [v, w, u]
  (v as first column, w and u fixed)
- f is **linear** → by duality, it equals a dot product: f(v) = p · v
- That hidden vector **p is exactly w × u**

## Why This Works
- Any linear map from 3D → 1D corresponds to a unique 3D vector (duality)
- The determinant measures **signed volume** of the parallelepiped
- So p · v = volume of the parallelepiped spanned by v, w, u
- Forces p to be: perpendicular to w and u, magnitude = area of their parallelogram

## Geometric Payoff
- The formula stops being a memorized determinant trick
- Cross product = the **vector that turns volume into a dot product**
- Direction (right-hand rule) falls out of the determinant's sign convention

## Connections to Prior Chapters
- Ch 6 (Determinant): volume scaling is the engine here
- Ch 9 (Duality): every linear functional ↔ a vector
- Ch 10 (Cross Product): same object, now *explained* instead of computed

## Quantum Computing Connection
- Duality between vectors and linear functionals is the **bra-ket structure**:
  ⟨ψ| is the dual (functional) of |ψ⟩
- Observables in QM are linear functionals on state space — same machinery
- Commutator [A, B] = AB − BA plays the role cross product plays in 3D geometry
