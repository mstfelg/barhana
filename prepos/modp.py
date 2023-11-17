'''
title: Modus Pollens
other_names: Law of detachment
'''

from sympy import symbols

from barhana.rules import dderiv, modp

p,q = symbols('p q')
pr = [
    p,
    p >> q,
]
conc = q

if cl0 := conc:
    st1 = modp(pr[0], pr[1])
    pf0 = dderiv(st1, cl0)
