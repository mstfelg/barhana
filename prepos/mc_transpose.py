'''
title: Transposition
desc: Assume P implies Q. Therefore ~Q implies ~P. And vice verse.
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, ideriv, iff, let_ante, theorem

p,q = symbols('p q')
pr = [
]
conc = iff(p >> q, ~q >> ~p)
thm = theorem(pr, conc)

if cl0 := conc:
    if1 = let_ante(cl0) # p >> q

    if cl1 := show_cons(cl0): # ~q >> ~p
        if2 = let_ante(cl1) # ~q
        st1 = modt(if1, if2) # ~p
        pf1 = dderiv(if2, st1)
