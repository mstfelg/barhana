'''
title: Unconjunction
desc: P and Q. Therefore P.
'''

from sympy import symbols

from barhana.rules import ideriv, let_not, modt, theorem
from conj_annul import conj_annul

p,q = symbols('p q')
pr = [
    p & q,
]
conc = p
unconj = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc: # p
        if1 = let_not(cl0) # ~p
        st1 = conj_annul(if1) # ~(p & q)
        pf0 = ideriv(if1, st1, pr[0])
