'''
title: Law of identity
other_names: Repeat rule
desc: P. Therefore P.
'''

from sympy import symbols

from barhana.rules import claim, dderiv, ideriv, let_not, theorem

p = symbols('p')
pr = [
    p
]
conc = p
rep = theorem(pr, conc)
