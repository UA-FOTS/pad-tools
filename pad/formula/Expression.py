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

    typeStr = {Type.AND: "&&",
               Type.OR: "||",
               Type.NOT: "~"}

    def __str__(self):
        if self.t == Expression.Type.NOT:
            return Expression.typeStr[Expression.Type.NOT] + "(" +\
                self.left.__str__() + ")"
        else:
            return "(" + self.left.__str__() + ") " +\
                Expression.typeStr[self.t] +\
                " (" + self.right.__str__() + ")"

    def dotLabel(self):
        return "[label=" + "\"" + Expression.typeStr[self.t] + "\"]"

    def dotStr(self):
        i = 0
        s = "graph Formula {\n"

        def _recDot(node):
            nonlocal i, s
            cur = i
            i += 1
            # recursive calls for expressions
            if isinstance(node, Expression):
                if node.left is not None:
                    leftNode = _recDot(node.left)
                if node.right is not None:
                    rightNode = _recDot(node.right)
                s += "n" + str(cur) + node.dotLabel() + ";\n"
                if node.left is not None:
                    s += "n" + str(cur) + " -- n" + str(leftNode) + ";\n"
                if node.right is not None:
                    s += "n" + str(cur) + " -- n" + str(rightNode) + ";\n"
            # otherwise, just make a node with a label
            else:
                s += "n" + str(cur) + "[label=\"" + str(node) + "\"];\n"
            return cur

        _recDot(self)
        s += "}"
        return s

    def dumpDot(self, fname):
        f = open(fname, "w")
        f.write(self.dotStr())
        f.close()


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

    typeStr = {Type.EQ: "=",
               Type.NEQ: "!=",
               Type.LE: "<",
               Type.LEQ: "<=",
               Type.GE: ">",
               Type.GEQ: ">=",
               Type.DIV: "%"}

    def __str__(self):
        return self.left.__str__() + " " + Predicate.typeStr[self.t] +\
            " " + self.right.__str__()

    def dotLabel(self):
        return "[shape=box,label=" + "\"" + Predicate.typeStr[self.t] + "\"]"
