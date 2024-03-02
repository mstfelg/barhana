'''
title: De Morgan's law
desc: P or Q iff ~(~P and ~Q)
'''

from sympy import symbols

from barhana.rules import (claim_cons, dneg, ideriv, iff, let_ante, let_not,
                           theorem)
from conj_unconj import unconj
from disj_syllo import mtp

p,q = symbols('p q')
pr = [
]
conc = iff(p | q, ~(~p & ~q))
conj_neg = theorem(pr, conc)
demorgans = theorem(pr, conc)

if cl0 := conc:
    if1 = let_ante(cl0) # p | q

    if cl1 := claim_cons(cl0): # ~(~p & ~q)
        if2 = dneg(let_not(cl1)) # ~p & ~q
        st1, st2 = unconj(if2) # ~p. ~q
        st3 = mtp(if1, st1) # q
        pf1 = ideriv(if2, st2, st3) #

    st1 = dderiv(if1, cl1) # first direction
