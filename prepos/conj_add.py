'''
title: Conjunction introduction
other_names: And introduction, Adjunction, Conjunction Addition.
desc: P. Q. Therefore P & Q.
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
    p,
    q
]
conc = p & q
conj = theorem(pr, conc)
