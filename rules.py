import sympy as sp
from sympy import Dummy, false, symbols, true
from sympy.logic.boolalg import And, Equivalent, Implies, Not


def thm_conc(prs, conc, *values):
    """
        Wraps prepositions and conclusion in a theorem.
    """
    thm_vars = conc.free_symbols
    thm_subs = {var: Dummy() for var in thm_vars}
    submap = dict(zip(thm_subs.keys(), values))

    for pr,val in zip(prs, values):
        if pr.subs(submap) != val:
            return false

    return conc.subs(submap)

def theorem(pr, conc):
    """
        Returns a function that can be used as a theorem.
    """

    return lambda *values: thm_conc(pr, conc, *values)

# Parsers

def prepos(expr):
    """
        Prepositions of an implication
    """

    if not isinstance(expr, Implies) or not isinstance(expr, Equivalent):
        return [false, false]

    return expr.args

# Rules

def rep(expr):
    """
        Identity
        Assume P. Therefore P.
    """

    return expr

def iff(lhs, rhs):
    """
        Biconditional
        lhs <=> rhs
    """

    return Equivalent(lhs,rhs)

def dneg(expr):
    """
        Double negation
        Assume P. Therefore not not P.
    """

    return ~~expr

# Claims and proofs
def claim(statement):
    """
        Claims a conclusion
    """

    return statement

def dderiv(claim_st, stat):
    """
        Direct Derivation
        Given a claim, statement is reached. Proof is concluded.
    """

    if claim_st != stat:
        return false

    return stat

def let_ante(cond):
    """
        Assume the antecedent of a conditional statement.
    """

    return prepos(cond)[0]

def let_cons(expr):
    """
        Assumes the consequent of a biconditional statement.
    """

    if not isinstance(expr, Equivalent):
        return false

    return prepos(expr)[1]

def claim_cons(cond):
    """
        Claim the consequence of a conditional statement.
    """

    return prepos(cond)[1]

def claim_not(statement):
    """
        Claims the negation of a statement
    """

    return ~statement

def ideriv(lhs, rhs):
    """
        Indirect Derivation (Proof by contradiction)
        Assume not P. Show P. Therefore P.
    """

    if lhs and rhs:
        return false

    return rhs

def let_not(statement):
    """
        Assume the negation of a claim.
    """

    return ~statement

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
        return [false, false]

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

    return false

def modt(expr, cons):
    """
        Modus Tollens
        Assume P. Assume Q implies P.
    """

    if prepos(expr)[1] == ~cons:
        return ~prepos(expr)[0]

    if prepos(cons)[1] == ~expr:
        return ~prepos(cons)[0]

    return false

def de_morgan(expr):
    """
        De Morgan's Law
    """

    if not isinstance(expr, Not):
        return false

    return (~ expr.args[0])^(~expr.args[1])

def vacuous(premise, expr):
    """
        Vacuous implication
        Assume P. Therefore not P implies Q.
    """

    return ~premise >> expr
