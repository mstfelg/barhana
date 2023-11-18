'''
title: Transivity of implication
other_names: Hypothetical syllogism, Chain Rule
'''

from sympy import symbols

from barhana.rules import dderiv, ideriv, let_ante, modp, modt

p,q,r = symbols('p q r')
pr = [
    p >> q,
    q >> r
]
conc = p >> r

if __name__ == '__main__':
    if cl0 := conc:
        if1 = let_ante(cl0) # p
        st1 = modp(if1, pr[0]) # q
        st2 = modp(st1, pr[1]) # r
        pf0 = dderiv(p, st2) # p >> r

    if cl0 := conc:
        cl1 = r
        if1 = ~r
        st2 = modt(if1, pr[0])
        st3 = modt(st2, pr[1])
        pf1 = ideriv(if1, st3)
