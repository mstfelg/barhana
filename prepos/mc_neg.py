'''
title: Material Condition Negation
'''

from sympy import symbols

from barhana.rules import (de_morgan, dneg, ideriv, let_not, theorem, unconj,
                           vacuous)

p,q = symbols('p q')
pr = [
    ~(p >> q)
]
conc = p & ~q
thm = theorem(pr, conc)

if cl0 := conc:
    if cl1 := unconj(cl0)[0]: # p
        if1 = let_not(cl1) # ~p
        st1 = vacuous(if1, q) # p >> q
        pf1 = ideriv(if1, st1, pr[0])

    if cl2 := unconj(cl0)[1]: # ~q
        if2 = dneg(let_not(cl2)) # q
