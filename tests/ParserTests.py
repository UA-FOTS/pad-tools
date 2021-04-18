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

import unittest

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from pad.parser.PADLexer import PADLexer
from pad.parser.FormulaBuilder import FormulaBuilder
from pad.parser.PADParser import PADParser


def parseFromString(s):
    lexer = PADLexer(InputStream(s))
    stream = CommonTokenStream(lexer)
    parser = PADParser(stream)
    tree = parser.formula()
    # we can traverse the concrete tree and create
    # our internal-representation tree now
    builder = FormulaBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)
    return builder.getFormula()


class ParserTests(unittest.TestCase):

    def testLinPoly1(self):
        formula = parseFromString("x1 > 10")
        self.assertTrue(formula.getExpression().eval({"x1": 20}))
        self.assertFalse(formula.getExpression().eval({"x1": 10}))

    def testLinPoly2(self):
        formula = parseFromString("x1 > 10 && x2 < x1")
        self.assertTrue(formula.getExpression().eval({"x1": 20, "x2": 10}))
        self.assertFalse(formula.getExpression().eval({"x1": 11, "x2": 11}))

    def testLinPoly3(self):
        formula = parseFromString("x1 > 10 && x2 < x1 || x3 % y")
        self.assertTrue(formula.getExpression().eval({"x1": 20,
                                                      "x2": 10,
                                                      "x3": 3,
                                                      "y": 5}))
        self.assertTrue(formula.getExpression().eval({"x1": 11,
                                                      "x2": 11,
                                                      "x3": 3,
                                                      "y": 9}))

    def testExpression1(self):
        formula = parseFromString("E x1 A y3 : x1=1 || ~(y3!=0) && x2<-3")
        self.assertEqual(str(formula.getExpression()),
                         "(x1 = 1) || ((~(y3 != 0)) && (x2 < -3))")

    def testExpression2(self):
        formula = parseFromString(
            "E x1 A y3 : x1=1 || ~(y3!=0) && 10* x1+ -5 * x2<-3")
        self.assertEqual(str(formula.getExpression()),
                         "(x1 = 1) || " +
                         "((~(y3 != 0)) && (10*x1 + -5*x2 < -3))")

    def testExpression3(self):
        formula = parseFromString(
            "E x1 A y3 : x1=1 || ~(y3!=0) && 10* x1+ -5 * x2<-3" +
            "|| (1 + 4) * x1 = 32")
        self.assertEqual(str(formula.getExpression()),
                         "((x1 = 1) || " +
                         "((~(y3 != 0)) && (10*x1 + -5*x2 < -3))) || " +
                         "(5*x1 = 32)")

    def testFormula1(self):
        formula = parseFromString("E x1 A y3 : x1=1 || ~(y3!=0) && x2<-3")
        self.assertEqual(str(formula), "E x1 A y3: " +
                         "(x1 = 1) || ((~(y3 != 0)) && (x2 < -3))")

    def testFormula2(self):
        formula = parseFromString(
            "E x1 E x2 : x1=1 || ~(y3!=0) && 10* x1+ -5 * x2<-3")
        self.assertEqual(str(formula), "E x1 E x2: " +
                         "(x1 = 1) || " +
                         "((~(y3 != 0)) && (10*x1 + -5*x2 < -3))")

    def testFormula3(self):
        formula = parseFromString(
            "E x1 A x2 A y3 : x1=1 || ~(y3!=0) && 10* x1+ -5 * x2<-3" +
            "|| (1 + 4) * x1 = 32")
        self.assertEqual(str(formula), "E x1 A x2 A y3: " +
                         "((x1 = 1) || " +
                         "((~(y3 != 0)) && (10*x1 + -5*x2 < -3))) || " +
                         "(5*x1 = 32)")


if __name__ == '__main__':
    unittest.main()
