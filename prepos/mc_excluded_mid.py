'''
title: Law of excluded middle
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = (p >> q) ^ (p >> ~q)
theorem = theorem(pr, conc)
