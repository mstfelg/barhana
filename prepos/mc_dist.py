from sympy import symbols

from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt, theorem)

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r)
]
conc = (p >> q) >> (p >> r)
thm = theorem(pr, conc)

if cl0 := conc:
    if1 = let_ante(cl0) # p >> q

    if cl1 := claim_cons(cl0): # p >> r
        if2 = let_ante(cl1) # p

        if cl2 := claim_cons(cl1): # r
            st1 = modp(if2, pr[0]) # q >> r

            if3 = let_not(cl2)
            st2 = modt(st1, if3) # ~q
            st3 = modt(if1, st2) # ~p
            pf2 = ideriv(cl2, st3) # r
        pf1 = cderiv(if2, cl2) # p >> r
    pf0 = dderiv(if1, cl1) # (p >> q) >> (p >> r)
