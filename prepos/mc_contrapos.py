'''
title: Material Condition Contraposition
'''

from sympy import symbols

from barhana.rules import (claim_cons, dderiv, dneg, ideriv, let_ante, let_not,
                           modp, theorem)

p,q = symbols('p q')
pr = [
    p >> q
]
conc = ~q >> ~p
contrapos = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc: # ~q >> ~p
        if1 = let_ante(cl0) # ~q

        if cl1 := claim_cons(cl0): # ~p
            if2 = let_not(cl1) # ~~p

            st1 = dneg(if2) # p
            st2 = modp(st1, pr[0]) # q
            pf1 = ideriv(if2, st2, if1)

        pf0 = dderiv(if1, cl1)
