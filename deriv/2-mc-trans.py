# desc: Hypothetical syllogism or Transivity of implication
# date: 2023-05-29

from sympy import symbols

p,q,r = symbols('p q r')
pr = [
    p >> q,
    q >> r
]
conc = p >> r

## Proof2

from barhana.rules import cderiv, modp

if1 = p
st1 = modp(if1, pr[0])
st2 = modp(st1, pr[1])
conc_pf = cderiv(p, st2)

## Proof1
# from barhana.rules import ideriv, modt
#
# cl1 = r
# if1 = ~r
# st2 = modt(if1, pr[0])
# st3 = modt(st2, pr[1])
# pf1 = ideriv(if1, st3)
