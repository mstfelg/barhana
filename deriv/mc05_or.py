# desc: Or-and-if material condition

from sympy import symbols

from barhana.rules import *

p,q = symbols('p q')
pr = [
    p >> q
]
conc = ~p ^ q
