# desc: Material Condition Contraposition

from sympy import symbols

from barhana.rules import (cderiv, dneg, ideriv, let_ante, let_not, modp,
                           show_cons)

p,q = symbols('p q')
pr = [
    p >> q
]
conc = ~q >> ~p

if if1 := let_ante(conc):
    cl1 = show_cons(conc)

    if if2 := let_not(cl1):
        st1 = dneg(if2)
        st2 = modp(st1, pr[0])
    pf1 = ideriv(st2, if1)
conc_pf = cderiv(if1, pf1)
