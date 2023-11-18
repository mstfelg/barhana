'''
title: Reduction of antecedents
'''

from sympy import symbols

from barhana.rules import (claim_cons, dderiv, ideriv, let_ante, let_not, modp,
                           modt, theorem)

p,q = symbols('p q')
pr = [
        p >> (p >> q)
]
conc = p >> q
mc_reduct = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc:
        if1 = let_ante(cl0) # p

        if cl1 := claim_cons(cl0): # q
            st1 = modp(pr[0], if1) # p >> q
