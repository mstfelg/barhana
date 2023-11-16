'''
title: Strengthening of antecedent
other_names: Distributitivity
'''

from sympy import symbols

from barhana.rules import *

p,q,r = symbols('p q r')
pr = [
        p >> q
]
cl0 = (p & r) >> q
