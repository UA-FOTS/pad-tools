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


class Expression:
    class Type(Enum):
        AND = 1
        OR = 2
        NOT = 3

    def __init__(self, t, left, right=None):
        self.t = t
        self.left = left
        self.right = right

    def __and__(self, e):
        return Expression(Expression.Type.AND, self, e)

    def __or__(self, e):
        return Expression(Expression.Type.OR, self, e)

    def __invert__(self):
        return Expression(Expression.Type.NOT, self)

    def __str__(self):
        typeStr = {Expression.Type.AND: "&&",
                   Expression.Type.OR: "||",
                   Expression.Type.NOT: "~"}
        if self.t == Expression.Type.NOT:
            return typeStr[Expression.Type.NOT] + "(" +\
                self.left.__str__() + ")"
        else:
            return "(" + self.left.__str__() + ") " +\
                typeStr[self.t] + " (" + self.right.__str__() + ")"


class Predicate(Expression):
    class Type(Enum):
        EQ = 1
        NEQ = 2
        LE = 3
        LEQ = 4
        GE = 5
        GEQ = 6
        DIV = 7

    def __init__(self, t, left, right):
        self.t = t
        self.left = left
        self.right = right

    def __str__(self):
        typeStr = {Predicate.Type.EQ: "=",
                   Predicate.Type.NEQ: "!=",
                   Predicate.Type.LE: "<",
                   Predicate.Type.LEQ: "<=",
                   Predicate.Type.GE: ">",
                   Predicate.Type.GEQ: ">=",
                   Predicate.Type.DIV: "%"}
        return self.left.__str__() + " " + typeStr[self.t] +\
            " " + self.right.__str__()
