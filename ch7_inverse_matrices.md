# Chapter 7: Inverse Matrices, Column Space & Null Space

## Inverse Matrix
- A⁻¹ = transformation that undoes A
- A⁻¹A = Identity matrix (does nothing)
- Only exists when det(A) ≠ 0

## System of Equations
- Matrix problem: find vector x where Ax = v
- det(A) ≠ 0 → exactly one solution: x = A⁻¹v
- det(A) = 0 → no inverse, either 0 or infinite solutions

## Column Space
- All possible outputs of a transformation
- Full column space → transformation covers all of space
- Reduced column space → transformation squishes to line or plane

## Null Space (Kernel)
- All vectors that land on the origin after transformation
- det ≠ 0 → null space is just the origin
- det = 0 → null space is a line, plane etc.

## Rank
- Number of dimensions in the column space
- Rank 2 = output is a plane, Rank 1 = output is a line

## Quantum Computing Connection
- Quantum gates are invertible — det = 1, null space is just origin
- Running a quantum gate backwards = applying its inverse (unitary property)
