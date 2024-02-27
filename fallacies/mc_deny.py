'''
title: Denying the antecedent
desc: P >> Q. ~P. Not implies ~Q.
'''

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
conc = ((p >> q) & q) >> ~q
conc = ~conc
da = theorem(pr, conc)
