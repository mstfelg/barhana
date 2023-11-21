'''
title: Commutative law for conjunction
'''

from sympy import symbols

from barhana.rules import dderiv, iff, modt, theorem

p,q = symbols('p q')
pr = [
]
conc = iff(p & q,  q & p)
conj_commut = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc:
        st1 = modt(pr[0], pr[1])
        pf0 = dderiv(st1, cl0)
