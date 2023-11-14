# desc: Law of identity

from sympy import symbols

from barhana.rules import claim, dderiv, ideriv, let_not, theorem

p = symbols('p')
pr = [
    p
]
cl0 = p
thm = theorem(pr, cl0)

# Direct proof
cl1 = claim(cl0)
st1 = pr[0]
pf1 = dderiv(cl1, st1)

# Indirect proof: proof by contradiction
if1 = let_not(cl0)
pf1 = ideriv(if1, pr[0])
