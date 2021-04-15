# Generated from PAD.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PADParser import PADParser
else:
    from PADParser import PADParser

# This class defines a complete listener for a parse tree produced by PADParser.
class PADListener(ParseTreeListener):

    # Enter a parse tree produced by PADParser#formula.
    def enterFormula(self, ctx:PADParser.FormulaContext):
        pass

    # Exit a parse tree produced by PADParser#formula.
    def exitFormula(self, ctx:PADParser.FormulaContext):
        pass


    # Enter a parse tree produced by PADParser#quants.
    def enterQuants(self, ctx:PADParser.QuantsContext):
        pass

    # Exit a parse tree produced by PADParser#quants.
    def exitQuants(self, ctx:PADParser.QuantsContext):
        pass


    # Enter a parse tree produced by PADParser#qf_expr.
    def enterQf_expr(self, ctx:PADParser.Qf_exprContext):
        pass

    # Exit a parse tree produced by PADParser#qf_expr.
    def exitQf_expr(self, ctx:PADParser.Qf_exprContext):
        pass


    # Enter a parse tree produced by PADParser#predicate.
    def enterPredicate(self, ctx:PADParser.PredicateContext):
        pass

    # Exit a parse tree produced by PADParser#predicate.
    def exitPredicate(self, ctx:PADParser.PredicateContext):
        pass


    # Enter a parse tree produced by PADParser#polynomial.
    def enterPolynomial(self, ctx:PADParser.PolynomialContext):
        pass

    # Exit a parse tree produced by PADParser#polynomial.
    def exitPolynomial(self, ctx:PADParser.PolynomialContext):
        pass


    # Enter a parse tree produced by PADParser#atom.
    def enterAtom(self, ctx:PADParser.AtomContext):
        pass

    # Exit a parse tree produced by PADParser#atom.
    def exitAtom(self, ctx:PADParser.AtomContext):
        pass



del PADParser