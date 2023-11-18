'''
title: Reductio ad absurdum
other_names: Indirect derivation
'''

from sympy import symbols

from barhana.rules import claim_cons, dneg, ideriv, let_not, modp, theorem

p = symbols('p')
pr = [
    ~p >> p
]
conc = p
thm = theorem(pr, conc)

if cl0 := conc: # p
    if1 = let_not(cl0) # ~p
    st1 = modp(if1, pr[0]) # p
    st2 = ideriv(if1, st1) # ~~p
    pf0 = dneg(st2) # p
