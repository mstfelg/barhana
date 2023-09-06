# desc: Syllogism

from sympy import symbols

from barhana.rules import (cderiv, dderiv, ideriv, let_ante, let_not, modp,
                           modt, show_cons)

p,q,r = symbols('p q r')
pr = [
    p >> q
]
conc = (q >> r) >> (p >> r)

if if1 := let_ante(conc): # q >> r
    cl1 = show_cons(conc) # p >> r

    if if2 := let_ante(cl1): # p
        cl2 = show_cons(cl1) # r

        if if3 := let_not(r):
            st1 = modt(cl1, if3) # ~p
        pf2 = ideriv(if2, st1)
    pf1 = cderiv(if2, pf2)
pf_conc = dderiv(cl1, pf1)
