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

from enum import Enum


class Formula:
    class QuantType(Enum):
        UNIV = 1
        EXIST = 2

    def __init__(self):
        self.quants = []
        self.quantd = set()
        self.qfexpr = None

    def setExpression(self, expr):
        self.qfexpr = expr

    def getExpression(self):
        return self.qfexpr

    def addQuant(self, t, var):
        if var in self.quantd:
            raise Exception("Quantified " + var + " more than once!")
        self.quants.append((t, var))
        self.quantd.add(var)

    def __str__(self):
        quantType = {Formula.QuantType.UNIV: "A",
                     Formula.QuantType.EXIST: "E"}
        qs = [quantType[t] + " " + var for (t, var) in self.quants]
        return " ".join(qs) + ": " + self.qfexpr.__str__()
