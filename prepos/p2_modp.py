# desc: Modus Pollens equivalent form

from sympy import symbols

from barhana.rules import dderiv, let_ante, modp, show_cons

p,q = symbols('p q')
pr = [
    p
]
conc = (p >> q) >> q

if if1 := let_ante(conc): # p >> q
    cl1 = show_cons(conc) # q
    st1 = modp(if1, pr[0]) # q
pf1 = dderiv(cl1, st1)
