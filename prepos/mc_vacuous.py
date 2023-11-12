'''
desc: Vacuous implication
Assume P. Therefore, ~P implies anything.
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, let_ante, theorem

p,q = symbols('p q')
pr = [
    p
]
cl0 = ~p >> q
thm = theorem(pr, cl0)

if if1 := let_ante(cl0):
    cl1 = claim_cons(cl0)
pf1 = ideriv(if1, pr[0])
