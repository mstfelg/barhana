# desc: Law of excluded middle

from sympy import symbols

from barhana.rules import theorem

p,q = symbols('p q')
pr = [
]
cl0 = (p >> q) ^ (p >> ~q)
theorem = theorem(pr, cl0)
