'''
title: Material condition law of annulment
other_names: Vacuous implication
desc: Assume P. Therefore, ~P implies anything.
'''

from sympy import symbols

from barhana.rules import claim_cons, ideriv, let_ante, theorem

p,q = symbols('p q')
pr = [
    p
]
conc = ~p >> q
vacuous = theorem(pr, conc)

if __name__ == '__main__':
    if cl0 := conc:
        if1 = let_ante(cl0)

        if cl1 := claim_cons(cl0):
            pf1 = ideriv(if1, pr[0])
