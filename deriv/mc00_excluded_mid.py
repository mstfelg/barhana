# desc: Law of excluded middle

from sympy import symbols

p,q = symbols('p q')
pr = [
]
conc = (p >> q) ^ (p >> ~q)
