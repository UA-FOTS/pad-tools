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


class LinearPolynomial:
    def __init__(self, coeffs):
        self.poly = coeffs

    def negate(self):
        for k in self.poly:
            self.poly[k] *= -1

    def eval(self, val):
        total = 0
        for k in self.poly:
            if k == "":
                total += self.poly[k]
            else:
                total += self.poly[k] * val[k]
        return total

    def __add__(self, f):
        g = dict(self.poly)
        for k in f.poly:
            if k in self.poly:
                g[k] += f.poly[k]
            else:
                g[k] = f.poly[k]
        return LinearPolynomial(g)

    def __sub__(self, f):
        g = dict(self.poly)
        for k in f.poly:
            if k in self.poly:
                g[k] -= f.poly[k]
            else:
                g[k] = f.poly[k]
        return LinearPolynomial(g)

    def __mul__(self, f):
        # Either self is a constant polynomial
        if len(self.poly.keys()) == 1 and "" in self.poly:
            g = dict(f.poly)
            for k in f.poly:
                g[k] *= self.poly[""]
            return LinearPolynomial(g)
        # or f is the constant
        elif len(f.poly.keys()) == 1 and "" in f.poly:
            f = dict(self.poly)
            for k in self.poly:
                g[k] *= f.poly[""]
            return LinearPolynomial(g)
        else:
            raise Exception("Found a nonlinear polynomial!")

    def __str__(self):
        def coeffStr(c):
            if c == 1:
                return ""
            elif c == -1:
                return "-"
            else:
                return str(c) + "*"
        monomials = [coeffStr(self.poly[k]) + k
                     for k in sorted(self.poly)
                     if k != ""]
        if "" in self.poly:
            monomials.append(str(self.poly[""]))
        return " + ".join(monomials)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.poly == other.poly
