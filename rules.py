import sympy as sp
from sympy import symbols
from sympy.logic.boolalg import And, Implies, Not


def prepos(expr):
    """ Prepositions of an implication """

    if not isinstance(expr, Implies):
        return [False, False]

    return expr.args

def unconj(expr):
    """ Conjunction Elimination """

    if not isinstance(expr, And):
        return [False, False]

    return expr.args


def dderiv(lhs, rhs):
    """ Direct Derivation """

    if (lhs != rhs):
        return False

    return lhs

def let_not(claim):
    return ~claim

def ideriv(lhs, rhs):
    """
        Indirect Derivation (Contradiction)
        Assuming LHS, we reached its negation, RHS. Therefore, RHS.
    """

    if (lhs == rhs):
        return False

    return rhs

def let_ante(cond):
    return prepos(cond)[0]

def show_cons(cond):
    return prepos(cond)[1]

def cderiv(lhs, rhs):
    """
        Conditional Derivation (Contradiction)
        Assuming lhs, we reached rhs. Therefore lhs >> rhs.
    """

    return lhs >> rhs

def dneg(expr):
    """ Double negation """

    return ~~expr

def modp(ante, expr):
    """ Modus Pollens """

    if prepos(expr)[0] == ante:
        return prepos(expr)[1]

    if prepos(ante)[0] == expr:
        return prepos(ante)[1]

def modt(expr, cons):
    """ Modus Tollens """

    if prepos(expr)[1] == ~cons:
        return ~prepos(expr)[0]

    if prepos(cons)[1] == ~expr:
        return ~prepos(cons)[0]

def rep(expr):
    """ Identity """

    return expr

def demorgan(expr):
    if not isinstance(expr, Not):
        return False

    return (~ expr.args[0])^(~expr.args[1])

def vacuous(premise, expr):
    return ~premise >> expr
