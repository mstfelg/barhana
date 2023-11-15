'''
desc: Modus Pollens
Law of detachment
'''

from sympy import symbols

from barhana.rules import dderiv, modp

p,q = symbols('p q')
pr = [
    p,
    p >> q,
]
cl0 = q

st1 = modp(pr[0], pr[1])
pf0 = dderiv(st1, cl0)
