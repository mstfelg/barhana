# desc: Material Condition Vacuous Conditional

from sympy import symbols

from barhana.rules import demorgan, ideriv, let_ante

p,q = symbols('p q')
pr = [
    ~p
]
conc = p >> q

if1 = let_ante(conc)
conc_pf = ideriv(if1, pr[0])
