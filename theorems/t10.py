from sympy import symbols

from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)

p,q,r = symbols('p q')
pr = [
    (p >> q) >> q
]
cl0 = (q >> p) >> p

if if1 := let_ante(cl0): # q >> p
    cl1 = claim_cons(cl0) # p

    if if2 := let_not(cl1): # ~p
        st1 = modt(if1, if2) # ~q
        st2 = modt(pr[0], st1) # ~(p >> q)
        cl2 = p >> q

        if if3 := let_ante(cl2): # p
            cl3 = claim_cons(cl2) # q
        pf2 = ideriv(if3, if2) # p >> q
    pf1 = ideriv(st2, pf2) # p
pf0 = dderiv(pf1, if1) # q >> p
