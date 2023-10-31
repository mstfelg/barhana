# desc: Law of excluded middle

from sympy import symbols

p,q = symbols('p q')
pr = [
]
cl0 = (p >> q) ^ (p >> ~q)
