# desc: Modus Pollens equivalent form

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, modp

p,q = symbols('p q')
pr = [
    q
]
cl0 = q >> (p >> q)

if if1 := let_ante(cl0): # q
    cl1 = claim_cons(cl0) # p >> q

    if if2 := let_ante(cl1): # p
        cl2 = claim_cons(cl1) # q
        pf2 = dderiv(cl2, if1) # q
    pf1 = dderiv(cl1, dderiv)
pf0 = dderiv(if1, cl1) # q >> (p >> q)
