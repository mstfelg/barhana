# desc: Modus Pollens equivalent form

from sympy import symbols

from barhana.rules import claim_cons, dderiv, let_ante, modp

p,q = symbols('p q')
pr = [
    p
]
cl0 = (p >> q) >> q

if if1 := let_ante(cl0): # p >> q
    cl1 = claim_cons(cl0) # q
    st1 = modp(if1, pr[0]) # q
pf1 = dderiv(cl1, st1)
