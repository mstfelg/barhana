# desc: Law of identity

from sympy import symbols

from barhana.rules import dderiv, show_conc

p = symbols('p')
pr = [
    p
]
conc = p
cl1 = show_conc(conc)
st1 = pr[0]
pf1 = dderiv(cl1, st1)