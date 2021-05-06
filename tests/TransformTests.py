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

from pad.formula.Formula import Formula


def parseFromString(s):
    return Formula.fromString(s)


class TransformTests(unittest.TestCase):

    def testNNF1(self):
        formula = parseFromString("x1 > 10 && ~(x2 <= x1)")
        nnfExp = formula.getExpression().NNF()
        self.assertEqual(str(nnfExp), "(x1 > 10) && (x2 > x1)")

    def testNNF2(self):
        formula = parseFromString("~(~(~(x1 > 10 && ~(x2 <= x1))))")
        nnfExp = formula.getExpression().NNF()
        self.assertEqual(str(nnfExp), "(x1 <= 10) || (x2 <= x1)")

    def testNNF3(self):
        formula = parseFromString("~(x1 > 10 || y + 32 = 5) && ~(x2 <= x1)")
        nnfExp = formula.getExpression().NNF()
        self.assertEqual(str(nnfExp),
                         "((x1 <= 10) && (y + 32 != 5)) && (x2 > x1)")

    def testLNNF1(self):
        formula = parseFromString("E x1 A y3: (x1 = 1) || ((~(y3 != 0)) "
                                  "&& (10*x1 + -5*x2 < -3))")
        nnfExp = formula.getExpression().NNF(LNNF=True)
        self.assertEqual(str(nnfExp),
                         "(x1 = 1) || ((y3 = 0) "
                         "&& (10*x1 + -5*x2 + 1 <= -3))")

    def testLNNF2(self):
        formula = parseFromString("((x1 = 1) || ((~(y3 != 0)) && (10*x1 "
                                  "+ -5*x2 < -3))) || (~(-52*x1 + y3 % "
                                  "-10*x2))")
        nnfExp = formula.getExpression().NNF(LNNF=True)
        self.assertEqual(str(nnfExp),
                         "((x1 = 1) || ((y3 = 0) && (10*x1 + -5*x2 + "
                         "1 <= -3))) || (((-52*x1 + y3 = 0) && ((-52*x1 "
                         "+ y3 + 1 <= -10*x2) || (-10*x2 + 1 <= -52*x1 "
                         "+ y3))) || (((-52*x1 + y3 = _new0 + _new1) && "
                         "(-52*x1 + y3 % _new0)) && (((1 <= _new1) && "
                         "(_new1 <= -52*x1 + y3 + -1)) || ((1 <= _new1) "
                         "&& (_new1 <= 52*x1 + -y3 + -1)))))")

    def testDNF1(self):
        formula = parseFromString("x1 > 10 && ~(x2 <= x1)")
        dnfExp = formula.getExpression().DNF()
        self.assertEqual(str(dnfExp), "(x1 > 10) && (x2 > x1)")

    def testDNF2(self):
        formula = parseFromString("x1 > 10 && (x2 <= x1 || x1 != y3)")
        dnfExp = formula.getExpression().DNF()
        self.assertEqual(str(dnfExp),
                         "((x1 > 10) && (x2 <= x1)) || "
                         "((x1 > 10) && (x1 != y3))")

    def testDNF3(self):
        formula = parseFromString("x1 > 10 && x2 <= x1 || y1 != x1")
        dnfExp = formula.getExpression().DNF()
        self.assertEqual(str(dnfExp),
                         "((x1 > 10) && (x2 <= x1)) || (y1 != x1)")


if __name__ == '__main__':
    unittest.main()
