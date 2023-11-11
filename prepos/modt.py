# desc: Modus Tollens

from sympy import symbols

from barhana.rules import dderiv, modt

p,q = symbols('p q')
pr = [
    ~q,
    p >> q,
]
cl0 = ~p

st1 = modt(pr[0], pr[1])
pf0 = dderiv(st1, cl0)
