# Chapter 13: Change of Basis

## Core Idea
- Coordinates are **language** — they only mean something relative to a chosen basis
- Our (2, 1) and Jennifer's (2, 1) point to **different vectors in space**
  because we're using different î, ĵ
- A "change of basis" is a translator between these languages

## The Change-of-Basis Matrix
- To translate **from Jennifer's coords → our coords**:
  multiply by the matrix whose **columns are her basis vectors written in our coords**
- To go the **other way** (our coords → her coords): multiply by the **inverse**
- Geometrically, this is the same linear transformation we've been studying —
  it just *reinterprets* the same vector in a new language

## Translating Transformations
- A matrix M in our basis is **not** the same matrix in Jennifer's basis
- To express our transformation in Jennifer's language:
  **A⁻¹ M A**
  - A: Jennifer → us (move into our coords)
  - M: apply the transformation in our language
  - A⁻¹: translate the result back into hers
- This sandwich pattern shows up everywhere — it means "same transformation,
  different perspective"

## Key Takeaway
- Linear transformations exist **independent of any basis**
- Matrices are just numeric *shadows* of them, cast by the basis you pick
- Choosing a smart basis can make a hard matrix become diagonal (next chapter!)

## Connections to Prior Chapters
- Ch 3 (Linear Transformations): the transformation is basis-free; the matrix isn't
- Ch 4 (Matrix Multiplication): A⁻¹ M A is composition read right-to-left
- Ch 7 (Inverse Matrices): the inverse is literally the reverse translator

## Quantum Computing Connection
- **Measurement bases**: measuring in the Z-basis vs. X-basis is exactly a change
  of basis — same quantum state, different coordinate readout
- Unitary U acts as the change-of-basis matrix between two orthonormal bases
- The **A⁻¹ M A** pattern is **U† M U** in QM — how operators transform between
  the Schrödinger and Heisenberg pictures, or between any two measurement bases
- Sets up **diagonalization** (Ch 14) — the foundation of spectral decomposition
  and observable eigenvalues
