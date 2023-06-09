# desc: Material Condition Import/Export

from sympy import symbols

from barhana.rules import cderiv, let_ante, modp, show_cons, unconj

p,q,r = symbols('p q r')
pr = [
    p >> (q >> r),
]
conc = (p & q) >> r

if1 = let_ante(conc)
cl1 = show_cons(conc)
st1,st2 = unconj(cl1)
st3 = modp(st1, pr[0])
st4 = modp(st3, st2)
conc_pf = cderiv(if1, st4)
