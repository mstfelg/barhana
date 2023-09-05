# desc: Distributitivity

from sympy import symbols

from barhana.rules import *

p,q,r = symbols('p q r')
pr = [
    r >> (p >> q)
]
conc = (r >> p) >> (r >> q)
