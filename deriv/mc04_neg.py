# desc: Material Condition Negation

from sympy import symbols

from barhana.rules import de_morgan, ideriv, let_not, unconj, vacuous

p,q = symbols('p q')
pr = [
    ~(p >> q)
]
conc = p & ~q

cl1 = unconj(conc)[0]

if if1 := let_not(cl1):
    st1 = vacuous(if1, q)
    pf1 = ideriv(st1, pr[0])

cl2 = unconj(conc)[1]
if2 = let_not(cl2)
