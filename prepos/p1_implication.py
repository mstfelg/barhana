# desc: Law of implication

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, theorem

p,q = symbols('p q')
pr = [
    q
]
cl0 = p >> q
thm = theorem(pr, cl0)

if if1 := let_ante(cl0):
    cl1 = claim_cons(cl0)
pf1 = dderiv(cl1, pr[0])
