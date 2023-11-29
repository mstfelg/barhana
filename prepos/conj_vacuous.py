'''
title: Vacuous conjunction
desc: ~P. Therefore ~(P & Q).
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
    ~p
]
conc = ~(p & q)
conj_vacuous = theorem(pr, conc)
