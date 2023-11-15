'''
desc: Transivity of implication
other_names: Hypothetical syllogism, Chain Rule
'''

from sympy import symbols

from barhana.rules import cderiv, ideriv, let_ante, modp, modt

p,q,r = symbols('p q r')
pr = [
    p >> q,
    q >> r
]
cl0 = p >> r

def main(*args):
    if args[0] == 'pf1':
        if if1 := let_ante(cl0): # p
            st1 = modp(if1, pr[0])
            st2 = modp(st1, pr[1])
        pf0 = cderiv(p, st2)

    if args[0] == 'pf2':
        cl1 = r
        if1 = ~r
        st2 = modt(if1, pr[0])
        st3 = modt(st2, pr[1])
        pf1 = ideriv(if1, st3)
