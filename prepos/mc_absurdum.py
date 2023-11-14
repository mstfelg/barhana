'''
desc: Reductio ad absurdum
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, let_ante, theorem

p = symbols('p')
pr = [
    ~p >> p
]
cl0 = p
thm = theorem(pr, cl0)
