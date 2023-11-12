from sympy import symbols

from barhana.rules import (cderiv, claim_cons, dderiv, ideriv, let_ante,
                           let_not, modp, modt)

p,q,r = symbols('p q')
pr = [
        p >> (p >> q)
]
cl0 = p >> q

if if1 := let_ante(cl0): # p
    cl1 = claim_cons(cl0) # q
    st1 = modp(pr[0], if1) # p >> q
    pf1 = modp(st1, if1) # p >> q
pf0 = dderiv(cl1, pf1) # p >> q
