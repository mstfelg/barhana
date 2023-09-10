# desc: Law of implication

from sympy import symbols

from barhana.rules import dderiv, let_ante, claim_cons

p,q = symbols('p q')
pr = [
    q
]
conc = p >> q

if if1 := let_ante(conc):
    cl1 = claim_cons(conc)
pf1 = dderiv(cl1, pr[0])
