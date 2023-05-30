# desc: Modus Tollens

from sympy import symbols

from barhana.rules import dderiv, modp

p,q = symbols('p q')
pr = [
    p,
    p >> q,
]
conc = q

st1 = modp(pr[0], pr[1])
conc_pf = dderiv(st1, conc)
