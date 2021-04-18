"""
Copyright 2021 Guillermo A. Perez

This file is part of pad-tools.

pad-tools is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pad-tools is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pad-tools. If not, see <https://www.gnu.org/licenses/>.
"""

from antlr4 import CommonTokenStream, FileStream, InputStream, ParseTreeWalker
from collections import OrderedDict
from enum import Enum

from ..parser.PADLexer import PADLexer
from ..parser.PADListener import PADListener
from ..parser.PADParser import PADParser
from .Expression import Predicate
from .LinearPolynomial import LinearPolynomial


class Formula:
    class QuantType(Enum):
        UNIV = 1
        EXIST = 2

    def __init__(self):
        self.quants = OrderedDict()
        self.quantd = set()
        self.qfexpr = None

    def setExpression(self, expr):
        self.qfexpr = expr

    def getExpression(self):
        return self.qfexpr

    def addQuant(self, t, var):
        if var in self.quantd:
            raise Exception("Quantified " + var + " more than once!")
        self.quants[var] = t
        self.quantd.add(var)

    def __str__(self):
        quantType = {Formula.QuantType.UNIV: "A",
                     Formula.QuantType.EXIST: "E"}
        qs = [quantType[t] + " " + var for var, t in self.quants.items()]
        return " ".join(qs) + ": " + self.qfexpr.__str__()

    def fromFile(fname):
        ins = FileStream(fname)
        lexer = PADLexer(ins)
        stream = CommonTokenStream(lexer)
        parser = PADParser(stream)
        tree = parser.formula()
        builder = FormulaBuilder()
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getFormula()

    def fromString(s):
        ins = InputStream(s)
        lexer = PADLexer(ins)
        stream = CommonTokenStream(lexer)
        parser = PADParser(stream)
        tree = parser.formula()
        builder = FormulaBuilder()
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getFormula()


class FormulaBuilder(PADListener):
    def __init__(self):
        self.formula = Formula()

    def getFormula(self):
        return self.formula

    def exitUnaInt(self, ctx):
        coefficient = int(ctx.INT().getText())
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({"": coefficient})

    def exitUnaVar(self, ctx):
        coefficient = 1
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({ctx.VARIABLE().getText(): coefficient})

    def exitUnaPoly(self, ctx):
        ctx.poly = ctx.polynomial().poly
        if ctx.neg is not None:
            ctx.poly.negate()

    def exitSumPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly + ctx.polynomial(1).poly

    def exitSubPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly - ctx.polynomial(1).poly

    def exitMultPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly * ctx.polynomial(1).poly

    def exitPred(self, ctx):
        predType = {"=": Predicate.Type.EQ,
                    "!=": Predicate.Type.NEQ,
                    "<": Predicate.Type.LE,
                    "<=": Predicate.Type.LEQ,
                    ">": Predicate.Type.GE,
                    ">=": Predicate.Type.GEQ,
                    "%": Predicate.Type.DIV}
        ctx.expr = Predicate(predType[ctx.BINOP().getText()],
                             ctx.polynomial(0).poly,
                             ctx.polynomial(1).poly)

    def exitAndQFExpr(self, ctx):
        ctx.expr = ctx.qfexpr(0).expr & ctx.qfexpr(1).expr

    def exitOrQFExpr(self, ctx):
        ctx.expr = ctx.qfexpr(0).expr | ctx.qfexpr(1).expr

    def exitUnaQFExpr(self, ctx):
        ctx.expr = ctx.qfexpr().expr
        if ctx.neg is not None:
            ctx.expr = ~ctx.qfexpr().expr

    def exitUnaPred(self, ctx):
        ctx.expr = ctx.predicate().expr
        if ctx.neg is not None:
            ctx.expr = ~ctx.predicate().expr

    def exitFormula(self, ctx):
        self.formula.setExpression(ctx.qfexpr().expr)

    def addQuant(self, ctx):
        quantType = {"A": Formula.QuantType.UNIV,
                     "E": Formula.QuantType.EXIST}
        self.formula.addQuant(quantType[ctx.QUANT().getText()],
                              ctx.VARIABLE().getText())

    def enterQuant(self, ctx):
        self.addQuant(ctx)

    def enterRecQuant(self, ctx):
        self.addQuant(ctx)
