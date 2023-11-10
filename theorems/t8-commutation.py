from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)
from sympy import symbols

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r)
]
cl0 = q >> (p >> r)

if if1 := let_ante(cl0): # q
    cl1 = claim_cons(cl0) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(cl1) # r

        st1 = modp(pr[0], if2) # q >> r

        if if3 := let_not(r):
            st2 = modt(st1, if3) # ~q
        pf2 = ideriv(st2, if1) # r
    pf1 = cderiv(if2, pf2) # p >> r
pf0 = dderiv(cl1, pf1) # (p >> q) >> (p >> r)
