'''
title: Vacuous consequent implication
desc: P. Therefore Q implies P.
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, theorem

p,q = symbols('p q')
pr = [
    p
]
conc = q >> p
vacons = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc:
        if1 = let_ante(cl0) # q

        if cl1 := claim_cons(cl0): # p
            pf1 = dderiv(cl1, pr[0])
