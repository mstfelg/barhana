# desc: Material Condition Contraposition

from sympy import symbols

from barhana.rules import (cderiv, dneg, ideriv, let_ante, let_not, modp,
                           claim_cons)

p,q = symbols('p q')
pr = [
    p >> q
]
cl0 = ~q >> ~p

if if1 := let_ante(cl0): # ~q
    cl1 = claim_cons(cl0) # ~p

    if if2 := let_not(cl1): # ~~p
        st1 = dneg(if2) # p
        st2 = modp(st1, pr[0]) # q
    pf1 = ideriv(st2, if1) # ~p
pf0 = cderiv(if1, pf1) # ~q >> ~p
