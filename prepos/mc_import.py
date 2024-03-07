'''
title: Material Condition Import
other_names: Importation
'''

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, modp, theorem, unconj

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r),
]
conc = (p & q) >> r
mc_import = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc: # (p & q) >> r
        if1 = let_ante(cl0) # p & q

        if cl1 := claim_cons(cl0): # r
            st1,st2 = unconj(cl1) # p, q
            st3 = modp(st1, pr[0]) # q >> r
            pf1 = modp(st3, st2)
        pf0 = dderiv(if1, cl1)
