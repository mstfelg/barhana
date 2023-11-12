'''
desc: Transposition
Assume P implies Q. Therefore ~Q implies ~P. And vice verse.
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, iff, let_ante, theorem, dderiv

p,q = symbols('p q')
pr = [
]
cl0 = iff(p >> q, ~q >> ~p)
thm = theorem(pr, cl0)

if if1 := let_ante(cl0): # p >> q
    cl1 = show_cons(cl0) # ~q >> ~p
    if if2 := let_ante(cl1): # ~q
        st1 = modt(if1, if2) # ~p
        pf1 = dderiv(if2, st1)
