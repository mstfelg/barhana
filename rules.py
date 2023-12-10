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

def dderiv(ante, cons):
    """
        Direct Derivation
        Assuming P, consequent Q is true. Therefore P >> Q.
    """

    return ante >> cons

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

def ideriv(ante, *imp):
    """
        Indirect Derivation (Proof by contradiction)
        Assuming P, statements ~Q and Q hold. Therefore ~P.

        Alternatively,
        Assuming P, statement ~P hold. Therefore ~P.
    """

    if len(imp) == 1:
        not_ante = imp[0]

        if ante != ~not_ante & ~ante != not_ante:
            return false

        return ~ante

    cons = imp[0]
    not_cons = imp[1]

    if cons != ~not_cons & ~cons != not_cons:
        return false

    return ~ante


def let_not(statement):
    """
        Assume the negation of a claim.
    """

    return ~statement

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

    return (~ expr.args[0]) | (~expr.args[1])

def vacuous(premise, expr):
    """
        Vacuous implication
        Assume P. Therefore not P implies Q.
    """

    return ~premise >> expr
