import sympy as sp
from sympy import symbols
from sympy.logic.boolalg import And, Implies, Not

# Parsers

def prepos(expr):
    """
        Prepositions of an implication
    """

    if not isinstance(expr, Implies):
        return [False, False]

    return expr.args

# Rules

def rep(expr):
    """
        Identity
        Assume P. Therefore P.
    """

    return expr

def dneg(expr):
    """
        Double negation
        Assume P. Therefore not not P.
    """

    return ~~expr

# Claims and proofs
def show_conc(claim):
    """
        Claims a conclusion
    """

    return claim

def dderiv(lhs, rhs):
    """
        Direct Derivation
        Assume P. Show Q. Therefore P implies Q.
    """

    if lhs != rhs:
        return False

    return lhs

def let_ante(cond):
    """
        Assume the antecedent of a conditional statement.
    """

    return prepos(cond)[0]

def show_cons(cond):
    """
        Claim the consequence of a conditional statement.
    """

    return prepos(cond)[1]

def ideriv(lhs, rhs):
    """
        Indirect Derivation (Proof by contradiction)
        Assume not P. Show P. Therefore P.
    """

    if lhs == rhs:
        return False

    return rhs

def let_not(claim):
    """
        Assume the negation of a claim.
    """

    return ~claim

def cderiv(lhs, rhs):
    """
        Conditional Derivation
        Assume LHS. Show RHS. Therefore LHS implies RHS.
    """

    return lhs >> rhs

def unconj(expr):
    """
        Conjunction Elimination
        Assume P and Q. Therefore P.
    """

    if not isinstance(expr, And):
        return [False, False]

    return expr.args

def modp(ante, expr):
    """
        Modus Pollens
        Assume P. Assume P implies Q. Therefore Q.
    """

    if prepos(expr)[0] == ante:
        return prepos(expr)[1]

    if prepos(ante)[0] == expr:
        return prepos(ante)[1]

    return False

def modt(expr, cons):
    """
        Modus Tollens
        Assume P. Assume Q implies P.
    """

    if prepos(expr)[1] == ~cons:
        return ~prepos(expr)[0]

    if prepos(cons)[1] == ~expr:
        return ~prepos(cons)[0]

    return False

def de_morgan(expr):
    """
        De Morgan's Law
    """

    if not isinstance(expr, Not):
        return False

    return (~ expr.args[0])^(~expr.args[1])

def vacuous(premise, expr):
    """
        Vacuous implication
        Assume P. Therefore not P implies Q.
    """

    return ~premise >> expr
