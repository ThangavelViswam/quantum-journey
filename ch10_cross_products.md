# Chapter 10: Cross Products

## Core Concepts
- Cross product of two 3D vectors v and w produces a **new vector**
  (unlike dot product which gives a scalar)
- Resulting vector is **perpendicular** to both input vectors
- Magnitude = area of the parallelogram spanned by v and w
- Direction follows the **right-hand rule**

## Key Properties
- **Anti-commutative**: v × w = -(w × v), order matters!
- Parallel vectors → cross product = zero (parallelogram has no area)
- Computed using the 3×3 determinant trick with î, ĵ, k̂ unit vectors

## Connection to Determinant (Ch 6)
- Cross product magnitude is literally a determinant
- The 3×3 matrix setup is the same scaling/area concept from Ch 6

## Quantum Computing Connection
- Appears in **angular momentum**: L = r × p
- Bloch sphere rotations rely on cross product geometry
- Pauli matrix anti-commutativity mirrors cross product: [X,Y] = 2iZ
