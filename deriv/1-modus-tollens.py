# desc: Modus Tollens example

from sympy import symbols

from barhana.rules import dderiv, modt

p,q = symbols('p q')
pr = [
    ~q,
    p >> q,
]
conc = ~p

st1 = modt(pr[0], pr[1])
conc_pf = dderiv(st1, conc)
