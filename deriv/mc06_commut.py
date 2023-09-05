# desc: Commutativity of antecedents

from sympy import symbols

from barhana.rules import *

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r)
]
conc = q >> (p >> r)
