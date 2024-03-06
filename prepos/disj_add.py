'''
title: modus tollendo ponens (MTP)
other_names: Disjunctive syllogism
'''

from sympy import symbols

from barhana.rules import ideriv, let_not, theorem
from conj import conj
from demorgans import demorgans

p,q,r = symbols('p q')
pr = [
    p | q,
    ~p
]
conc = q
mtp = theorem(pr, conc)

if __name__ == "__main__":
    if cl0 := conc:
        if1 = let_not(cl0) # ~q
        st1 = conj(pr[2], if1) # ~p & ~q
        st2 = demorgans(st1) # ~(p | q)
        pf0 = ideriv(if1, st2, pr[1])
