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
from .LinearPolynomial import LinearPolynomial


class Expression:
    class Type(Enum):
        AND = 1
        OR = 2
        NOT = 3

    nextVar = 0

    def freshVars(amount):
        vs = []
        while len(vs) < amount:
            vname = "_new" + str(Expression.nextVar)
            vs.append(vname)
            Expression.nextVar += 1
        return tuple(vs)

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

    def _recDNF(node):
        if node.t not in [Expression.Type.AND,
                          Expression.Type.OR]:
            return node
        else:
            newLeft = node.left.DNF()
            newRight = node.right.DNF()
            if node.t == Expression.Type.AND:
                canDistribute = False
                if newLeft.t == Expression.Type.OR:
                    conjunct = newRight
                    disj1 = newLeft.left
                    disj2 = newLeft.right
                    canDistribute = True
                elif newRight.t == Expression.Type.OR:
                    conjunct = newLeft
                    disj1 = newRight.left
                    disj2 = newRight.right
                    canDistribute = True
                if canDistribute:
                    conj1 = Expression(Expression.Type.AND,
                                       conjunct, disj1)
                    conj2 = Expression(Expression.Type.AND,
                                       conjunct, disj2)
                    return Expression(Expression.Type.OR,
                                      conj1, conj2)
            return node

    def DNF(self):
        nnfExp = self.NNF()
        return Expression._recDNF(nnfExp)

    def NNF(self, neg=False, LNNF=False):
        if self.t == Expression.Type.NOT:
            return self.left.NNF(not neg, LNNF)
        else:
            newT = self.t
            if neg and self.t == Expression.Type.AND:
                newT = Expression.Type.OR
            elif neg and self.t == Expression.Type.OR:
                newT = Expression.Type.AND
            newLeft = self.left.NNF(neg, LNNF)
            newRight = self.right.NNF(neg, LNNF)
            return Expression(newT, newLeft, newRight)

    def LNF(self):
        lnnfExp = self.NNF(LNNF=True)
        return Expression._recDNF(lnnfExp)

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
                s += "n" + str(cur) + "[shape=plaintext,label=\"" +\
                    str(node) + "\"];\n"
            return cur

        _recDot(self)
        s += "}"
        return s

    def eval(self, val):
        if self.t == Expression.Type.NOT:
            return not self.left.eval(val)
        elif self.t == Expression.Type.AND:
            return self.left.eval(val) and self.right.eval(val)
        elif self.t == Expression.Type.OR:
            return self.left.eval(val) or self.right.eval(val)

    def dumpDot(self, fname):
        f = open(fname, "w")
        f.write(self.dotStr())
        f.close()


class Predicate(Expression):
    class Type(Enum):
        EQ = 4
        NEQ = 5
        LE = 6
        LEQ = 7
        GE = 8
        GEQ = 9
        DIV = 10

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

    def _NNF(self, neg=False):
        if not neg:
            return self
        elif self.t == Predicate.Type.EQ:
            return Predicate(Predicate.Type.NEQ, self.left, self.right)
        elif self.t == Predicate.Type.NEQ:
            return Predicate(Predicate.Type.EQ, self.left, self.right)
        elif self.t == Predicate.Type.LE:
            return Predicate(Predicate.Type.GEQ, self.left, self.right)
        elif self.t == Predicate.Type.LEQ:
            return Predicate(Predicate.Type.GE, self.left, self.right)
        elif self.t == Predicate.Type.GE:
            return Predicate(Predicate.Type.LEQ, self.left, self.right)
        elif self.t == Predicate.Type.GEQ:
            return Predicate(Predicate.Type.LE, self.left, self.right)
        elif self.t == Predicate.Type.DIV:
            return ~self

    def _LNNF(self, neg=False):
        if neg and self.t == Predicate.Type.DIV:
            # either the LHS is 0 and the right is not
            lhs0 = Predicate(Predicate.Type.EQ, self.left,
                             LinearPolynomial({"": 0}))
            rhsleq0 = Predicate(Predicate.Type.LEQ,
                                self.left + 1, self.right)
            rhsgeq0 = Predicate(Predicate.Type.LEQ,
                                self.right + 1, self.left)
            case1 = lhs0 & (rhsleq0 | rhsgeq0)
            # or we can quantify a non-zero remainder
            temp1, temp2 = Expression.freshVars(2)
            qrem = Predicate(Predicate.Type.EQ,
                             self.left, LinearPolynomial({temp1: 1, temp2: 1}))
            quot = Predicate(Predicate.Type.DIV,
                             self.left, LinearPolynomial({temp1: 1}))
            rempoly = LinearPolynomial({temp2: 1})
            g1 = Predicate(Predicate.Type.LEQ, LinearPolynomial({"": 1}),
                           rempoly)
            lf1 = Predicate(Predicate.Type.LEQ, rempoly, self.left - 1)
            lnf1 = Predicate(Predicate.Type.LEQ, rempoly, (self.left * -1) - 1)
            case2 = qrem & quot & ((g1 & lf1) | (g1 & lnf1))
            # return the disjunction
            return case1 | case2
        else:
            nnfNode = self._NNF(neg)
            if nnfNode.t == Predicate.Type.NEQ:
                leq = Predicate(Predicate.Type.LEQ,
                                nnfNode.left + 1, nnfNode.right)
                geq = Predicate(Predicate.Type.LEQ,
                                nnfNode.right + 1, nnfNode.left)
                return leq | geq
            elif nnfNode.t == Predicate.Type.LE:
                return Predicate(Predicate.Type.LEQ,
                                 nnfNode.left + 1, nnfNode.right)
            elif nnfNode.t == Predicate.Type.GE:
                return Predicate(Predicate.Type.LEQ,
                                 nnfNode.right + 1, nnfNode.left)
            elif nnfNode.t == Predicate.Type.GEQ:
                return Predicate(Predicate.Type.LEQ,
                                 nnfNode.right, nnfNode.left)
            else:
                return nnfNode

    def NNF(self, neg=False, LNNF=False):
        if LNNF:
            return self._LNNF(neg)
        else:
            return self._NNF(neg)

    def eval(self, val):
        leftPoly = self.left.eval(val)
        rightPoly = self.right.eval(val)
        if self.t == Predicate.Type.EQ:
            return leftPoly == rightPoly
        elif self.t == Predicate.Type.NEQ:
            return leftPoly != rightPoly
        elif self.t == Predicate.Type.LE:
            return leftPoly < rightPoly
        elif self.t == Predicate.Type.LEQ:
            return leftPoly <= rightPoly
        elif self.t == Predicate.Type.GE:
            return leftPoly > rightPoly
        elif self.t == Predicate.Type.GEQ:
            return leftPoly >= rightPoly
        elif self.t == Predicate.Type.DIV:
            return (rightPoly % leftPoly) == 0

    def dotLabel(self):
        return "[shape=box,label=" + "\"" + Predicate.typeStr[self.t] + "\"]"
