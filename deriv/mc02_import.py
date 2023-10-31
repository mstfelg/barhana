# desc: Material Condition Import/Export

from sympy import symbols

from barhana.rules import cderiv, claim_cons, let_ante, modp, unconj

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r),
]
cl0 = (p & q) >> r

if if1 := let_ante(cl0):
    cl1 = claim_cons(cl0)

    st1,st2 = unconj(cl1)
    st3 = modp(st1, pr[0])
    st4 = modp(st3, st2)
pf0 = cderiv(if1, st4)
