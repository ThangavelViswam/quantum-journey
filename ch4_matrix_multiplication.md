# Chapter 4: Matrix Multiplication as Composition

## Key Concepts
- Composition = applying one transformation after another
- e.g. first rotate, then shear = one combined transformation
- That combined transformation is captured by multiplying the two matrices

## Important Rules
- Read right to left — AB means apply B first, then A
- Matrix multiplication is NOT commutative — AB ≠ BA
- Associativity holds — (AB)C = A(BC)

## Example: Rotation then Shear
- Rotation matrix R = [0 -1 / 1 0]
- Shear matrix S = [1 1 / 0 1]
- R × S gives a new matrix capturing both transformations at once

## Quantum Computing Connection
- Applying multiple quantum gates in sequence = multiplying their matrices
- Order matters — same as reading right to left
