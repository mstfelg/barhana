# desc: Material Condition Vacuous Conditional

from sympy import symbols

from barhana.rules import ideriv, let_ante

p,q = symbols('p q')
pr = [
    ~p
]
cl0 = p >> q

if1 = let_ante(cl0)
pf0 = ideriv(if1, pr[0])
