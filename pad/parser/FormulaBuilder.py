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

from ..formula.LinearPolynomial import LinearPolynomial
from .PADListener import PADListener


class FormulaBuilder(PADListener):
    def exitUnaInt(self, ctx):
        coefficient = int(ctx.INT().getText())
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({"": coefficient})
        print(ctx.poly)

    def exitUnaVar(self, ctx):
        coefficient = 1
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({ctx.VARIABLE().getText(): coefficient})
        print("unavar " + str(ctx.poly))

    def exitUnaPoly(self, ctx):
        ctx.poly = ctx.polynomial().poly
        if ctx.neg is not None:
            ctx.poly.negate()
        print("unapoly " + str(ctx.poly))

    def exitSumPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly + ctx.polynomial(1).poly
        print("sum " + str(ctx.poly))

    def exitSubPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly - ctx.polynomial(1).poly
        print(ctx.poly)

    def exitMultPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly * ctx.polynomial(1).poly
        print("prod " + str(ctx.poly))
