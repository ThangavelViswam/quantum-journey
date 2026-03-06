# Chapter 3: Linear Transformations & Matrices

## What is a Linear Transformation?
- A function that takes a vector in → spits a vector out
- "Linear" means two rules must hold:
  - Lines stay lines (no curving)
  - Origin stays fixed

## Key Insight
- Only need to track where i-hat and j-hat land after transformation
- Those two landing spots become the columns of a matrix
- Don't memorize formulas — just think "where do the basis vectors land?"

## Matrix × Vector
- Applying a transformation to a vector
- [a b / c d] × [x / y] = [ax+by / cx+dy]

## Special Transformations
- Rotation matrix → rotates all of space by an angle
- Shear matrix → slants space
- Identity matrix → does nothing, vectors stay put

## Composition
- Applying one transformation after another = matrix multiplication

## Quantum Computing Connection
- Quantum gates (Hadamard, CNOT) are linear transformations
- Represented as matrices applied to qubit state vectors
- e.g. Hadamard gate puts a qubit into superposition — just a matrix multiplication
