'''
title: Modus Tollens
other_names: Indirect reasoning
'''

from sympy import symbols

from barhana.rules import dderiv, modt

p,q = symbols('p q')
pr = [
    ~q,
    p >> q,
]
conc = ~p
modt = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc:
        st1 = modt(pr[0], pr[1])
        pf0 = dderiv(st1, cl0)
