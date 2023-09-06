# title: Law of identity
# desc: proof by contradiction

from sympy import symbols

from barhana.rules import ideriv, let_not

p = symbols('p')
pr = [
    p
]
conc = p

if1 = let_not(conc)
pf1 = ideriv(if1, pr[0])
