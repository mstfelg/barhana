from sympy import symbols

from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)

p,q,r = symbols('p q r')
pr = [
    p >> q
]
cl0 = (q >> r) >> (p >> r)

if if1 := let_ante(cl0): # q >> r
    cl1 = claim_cons(cl0) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(cl1) # r

        if if3 := let_not(r):
            st1 = modt(cl1, if3) # ~p
        pf2 = ideriv(if2, st1) # r
    pf1 = cderiv(if2, pf2) # p >> r
pf0 = dderiv(cl1, pf1) # (q >> r) >> (p >> r)
