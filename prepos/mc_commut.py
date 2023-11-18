from sympy import symbols

from barhana.rules import (claim_cons, dderiv, ideriv, let_ante, let_not, modp,
                           modt, theorem)

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r)
]
conc = q >> (p >> r)
thm = theorem(pr, conc)

if cl0 := conc:
    if1 = let_ante(cl0) # q

    if cl1 := claim_cons(cl0): # p >> r
        if2 = let_ante(cl1) # p

        if cl2 := claim_cons(cl1): # r
            st1 = modp(pr[0], if2) # q >> r
            if3 = let_not(cl2) # ~r
            st2 = modt(st1, if3) # ~q
            pf2 = ideriv(if3, st2, if1) # r

        pf1 = dderiv(if2, cl2) # p >> r
    pf0 = dderiv(if1, cl1) # q >> (p >> r)
