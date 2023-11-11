from sympy import *

from prepos.p0_identity import thm as thm

p,q = symbols('x y')
e = thm(q)
print(e)
