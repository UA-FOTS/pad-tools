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


    # Enter a parse tree produced by PADParser#RecQuant.
    def enterRecQuant(self, ctx:PADParser.RecQuantContext):
        pass

    # Exit a parse tree produced by PADParser#RecQuant.
    def exitRecQuant(self, ctx:PADParser.RecQuantContext):
        pass


    # Enter a parse tree produced by PADParser#Quant.
    def enterQuant(self, ctx:PADParser.QuantContext):
        pass

    # Exit a parse tree produced by PADParser#Quant.
    def exitQuant(self, ctx:PADParser.QuantContext):
        pass


    # Enter a parse tree produced by PADParser#AndQFExpr.
    def enterAndQFExpr(self, ctx:PADParser.AndQFExprContext):
        pass

    # Exit a parse tree produced by PADParser#AndQFExpr.
    def exitAndQFExpr(self, ctx:PADParser.AndQFExprContext):
        pass


    # Enter a parse tree produced by PADParser#UnaQFExpr.
    def enterUnaQFExpr(self, ctx:PADParser.UnaQFExprContext):
        pass

    # Exit a parse tree produced by PADParser#UnaQFExpr.
    def exitUnaQFExpr(self, ctx:PADParser.UnaQFExprContext):
        pass


    # Enter a parse tree produced by PADParser#UnaPred.
    def enterUnaPred(self, ctx:PADParser.UnaPredContext):
        pass

    # Exit a parse tree produced by PADParser#UnaPred.
    def exitUnaPred(self, ctx:PADParser.UnaPredContext):
        pass


    # Enter a parse tree produced by PADParser#OrQFExpr.
    def enterOrQFExpr(self, ctx:PADParser.OrQFExprContext):
        pass

    # Exit a parse tree produced by PADParser#OrQFExpr.
    def exitOrQFExpr(self, ctx:PADParser.OrQFExprContext):
        pass


    # Enter a parse tree produced by PADParser#Pred.
    def enterPred(self, ctx:PADParser.PredContext):
        pass

    # Exit a parse tree produced by PADParser#Pred.
    def exitPred(self, ctx:PADParser.PredContext):
        pass


    # Enter a parse tree produced by PADParser#UnaInt.
    def enterUnaInt(self, ctx:PADParser.UnaIntContext):
        pass

    # Exit a parse tree produced by PADParser#UnaInt.
    def exitUnaInt(self, ctx:PADParser.UnaIntContext):
        pass


    # Enter a parse tree produced by PADParser#SumPoly.
    def enterSumPoly(self, ctx:PADParser.SumPolyContext):
        pass

    # Exit a parse tree produced by PADParser#SumPoly.
    def exitSumPoly(self, ctx:PADParser.SumPolyContext):
        pass


    # Enter a parse tree produced by PADParser#UnaPoly.
    def enterUnaPoly(self, ctx:PADParser.UnaPolyContext):
        pass

    # Exit a parse tree produced by PADParser#UnaPoly.
    def exitUnaPoly(self, ctx:PADParser.UnaPolyContext):
        pass


    # Enter a parse tree produced by PADParser#UnaVar.
    def enterUnaVar(self, ctx:PADParser.UnaVarContext):
        pass

    # Exit a parse tree produced by PADParser#UnaVar.
    def exitUnaVar(self, ctx:PADParser.UnaVarContext):
        pass


    # Enter a parse tree produced by PADParser#MultPoly.
    def enterMultPoly(self, ctx:PADParser.MultPolyContext):
        pass

    # Exit a parse tree produced by PADParser#MultPoly.
    def exitMultPoly(self, ctx:PADParser.MultPolyContext):
        pass


    # Enter a parse tree produced by PADParser#SubPoly.
    def enterSubPoly(self, ctx:PADParser.SubPolyContext):
        pass

    # Exit a parse tree produced by PADParser#SubPoly.
    def exitSubPoly(self, ctx:PADParser.SubPolyContext):
        pass



del PADParser