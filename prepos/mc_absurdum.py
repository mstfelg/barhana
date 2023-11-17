'''
title: Reductio ad absurdum
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, let_not, modp, theorem

p = symbols('p')
pr = [
    ~p >> p
]
conc = p
thm = theorem(pr, conc)

if cl0 := conc:
    if1 = let_not(cl0)
    st1 = modp(if1, pr[0])
    pf0 = ideriv(st1, if1)
