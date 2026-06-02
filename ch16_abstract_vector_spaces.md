# Chapter 16: Abstract Vector Spaces

## Core Idea
- "What *is* a vector, really?" — not just arrows or lists of numbers
- A vector is **anything that obeys the rules of vector addition and scaling**
- Functions, polynomials, matrices, quantum states — all are vectors in the right sense

## Functions as Vectors
- Add two functions: (f + g)(x) = f(x) + g(x)
- Scale a function: (c·f)(x) = c·f(x)
- These satisfy the same algebra as arrows in ℝⁿ
- So all of linear algebra — span, basis, linear maps, eigenvectors — applies to **functions**

## Linear Transformations on Functions
- A map L taking functions to functions is **linear** if:
  - L(f + g) = L(f) + L(g)
  - L(c·f) = c·L(f)
- The **derivative** d/dx is a linear transformation on the space of functions!
- It even has a **matrix representation** in the basis of polynomials {1, x, x², x³, ...}
  — an infinite matrix with the power-rule coefficients on a superdiagonal

## The Eight Axioms
A vector space is any set V with two operations (+, ·) satisfying:
1. Associativity of addition
2. Commutativity of addition
3. Additive identity (zero vector exists)
4. Additive inverses
5. Compatibility of scalar multiplication: a(bv) = (ab)v
6. Scalar multiplicative identity: 1·v = v
7. Distributivity over vector addition: a(u + v) = au + av
8. Distributivity over scalar addition: (a + b)v = av + bv

- Anything satisfying these gets **all the theorems for free**
- This is the **power of abstraction**: prove once, apply everywhere

## Why Abstraction Wins
- Mathematicians don't care *what* a vector is — only that it behaves like one
- The "arrows" picture is a useful crutch but not the truth
- The truth lives in the axioms — basis-free, picture-free, dimension-agnostic
- This is why physicists, computer scientists, and statisticians keep meeting
  in the same theorems from different directions

## Connections to Prior Chapters
- Ch 1–2: arrows and lists were just **two models** of the same abstract object
- Ch 3 (Linear Transformations): the *definition* (linearity) is what survives abstraction;
  the matrix representation is just a coordinate shadow
- Ch 13 (Change of Basis): "the transformation is basis-free" — this chapter formalizes that
- Ch 14 (Eigenvectors): eigen-functions of d/dx are exponentials (e^(λx)) — same idea, new home

## Quantum Computing Connection
- A **quantum state** lives in a **Hilbert space** — an abstract complex vector space
  with an inner product, possibly infinite-dimensional
- Wavefunctions ψ(x) are literally vectors in a function space
- **Operators** (position, momentum, Hamiltonian) are linear transformations on that space
- The **Schrödinger equation** iħ ∂ψ/∂t = Hψ is a linear ODE on Hilbert space —
  same eigenvector machinery as Ch 14, just with d/dt and H instead of A and λ
- **Qubit states** |ψ⟩ ∈ ℂ² are the finite-dimensional case; this whole series has been
  the warm-up for doing it in infinite dimensions

## Series Capstone
- Linear algebra is not about matrices — matrices are a **coordinate-dependent tool**
  for studying linear transformations on vector spaces
- The geometric pictures (Ch 1–15) build intuition; the axioms (Ch 16) are the truth
- Next stop: **functional analysis**, **Hilbert spaces**, and the full machinery of QM
