---
title: Barhana Tutorial
---

A logic problem consists of
1. Prepositions: `pr[0]`, assertion to be made true.
2. Claims: `cl0`, a statement that needs to be proved.
3. Assumptions: `if1`, a statement assumed to be true.
4. Statements: `st1`, for true statements.
5. Proof statement: `pf1`, a statement that concludes the proof of a claim.

The conclusion is the root claim (`cl0`). A claim is started by Python Walrus
Operator in an if-statement. This is used to structure the solution into
subclaims.

A proof statement is like a regular statement but signifies the end of a proof.
It can use any imported theorem, but usually it uses Direct Derivation `dderiv`
or Indirect Derivation `ideriv` for demonstrating the proof. Once a proof is
concluded, a claim can be used as a true statement.

## Direct Derivation
```python
pf2 = ideriv(if3, st2)
```
Assuming `if3`, statement `st2` is reached. Therefore `if3` implies `st2`.

## Indirect Derivation
```python
pf2 = ideriv(if3, st2, if1)
```

Assuming `if3`, we reached `st2`, but this contradicts
`if1`. Therefore (the return value of `ideriv`), not `if3`.
