'''
title: AND distributitivity over implication
'''

from sympy import symbols

from barhana.rules import (claim_cons, dderiv, dneg, ideriv, iff, let_ante,
                           let_not, modp, modt)

p,q,r = symbols('p q r')
pr = [
]
cl0 = iff(p & q >> r, p & ~r >> ~q)
