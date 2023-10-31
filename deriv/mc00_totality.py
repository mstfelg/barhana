# desc: Totality

from sympy import symbols

p,q,r = symbols('p q r')
pr = [
]
cl0 = (p >> q) ^ (q >> p)
