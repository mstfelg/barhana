'''
title: Commutativity of antecedents
'''

from sympy import symbols

from barhana.rules import *

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r)
]
cl0 = q >> (p >> r)
thm = theorem(pr, cl0)

if if1 := let_ante(cl0): # q
    cl1 = claim_cons(cl0) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(r) # r
        st1 = modp(pr[0], p) # q >> r
        st2 = modp(if1, st1) # r
    pf2 = dderiv(cl2, st2) # p >> r
pf1 = dderiv(cl1, pf2) # q >> (p >> r)
pf0 = dderiv(cl0, pf1)
