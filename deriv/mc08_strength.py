# desc: Distributitivity

from sympy import symbols

from barhana.rules import *

p,q,r = symbols('p q r')
pr = [
        p >> q
]
conc = (p & r) >> q
