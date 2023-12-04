'''
title: De Morgan's law
desc: P or Q iff ~(~P and ~Q)
'''

from sympy import symbols

from barhana.rules import theorem, iff

p,q = symbols('p q')
pr = [
]
conc = iff(p | q, ~(~p & ~q))
conj_neg = theorem(pr, conc)
