from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)
from sympy import symbols

p,q,r = symbols('p q r')
pr = [
        p >> (q >> r)
]
cl0 = (p >> q) >> (p >> r)

if if1 := let_ante(cl0): # p >> q
    cl1 = claim_cons(cl0) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(cl1) # r

        st1 = modp(if2, pr[0]) # q >> r

        if if3 := let_not(r):
            st2 = modt(st1, if3) # ~q
            st3 = modt(if1, st2) # ~p
        pf2 = ideriv(st3, if2) # r
    pf1 = cderiv(if2, pf2) # p >> r
pf0 = dderiv(cl1, pf1) # (p >> q) >> (p >> r)