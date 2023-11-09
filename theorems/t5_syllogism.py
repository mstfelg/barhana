from sympy import symbols

from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)

p,q,r = symbols('p q r')
pr = [
    q >> r
]
cl0 = (p >> q) >> (p >> r)

if if1 := let_ante(cl0): # p >> q
    cl1 = claim_cons(cl0) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(cl1) # r

        if if3 := let_not(r):
            st1 = modt(pr[0], if3) # ~q
            st2 = modt(st1, if1) # ~p
        pf2 = ideriv(st2, if2) # r
    pf1 = cderiv(if2, pf2) # p >> r
pf0 = dderiv(cl1, pf1) # (p >> q) >> (p >> r)
