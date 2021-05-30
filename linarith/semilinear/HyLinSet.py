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

import z3

from .utils import getGenerators, getBases, minAntichain


class HyLinSet:
    def __init__(self, A=None, b=None, C=None, d=None):
        """
        Computes the semilinear set of solutions solutions of a set of linear
        diophantine inequalities  Ax <= b and Cx = d.
        """
        if A is not None:
            assert b is not None
            n = len(A[0])
        else:
            assert C is not None
            assert d is not None
            n = len(C[0])
        generators = getGenerators(A, C)
        bases = getBases(A, b, C, d)
        generators_out = []
        bases_out = []
        for g in generators:
            generators_out.append(g[:n])
        for b in bases:
            bases_out.append(b[:n])
        self.bases = bases_out
        self.generators = minAntichain(generators_out)

    def __str__(self):
        return "Bases: " + str(self.bases) + "\n" +\
               "Generators: " + str(self.generators)

    def __contains__(self, vec):
        n = len(vec)
        if n != len(self.bases[0]):
            return False
        m = len(self.generators)
        vrs = [z3.Int("g%i" % i) for i in range(m)]
        solver = z3.Solver()
        # only nonnegative multiplicities of generators
        for i in range(m):
            solver.add(vrs[i] >= 0)
        # for some linear set, all dimensions sum up to
        # the given values
        linsets = []
        for b in self.bases:
            eqsys = []
            for i in range(n):
                term = b[i] + sum([self.generators[j][i] * vrs[j]
                                   for j in range(m)])
                eqsys.append(term == int(vec[i]))
            linsets.append(z3.And(eqsys))
        solver.add(z3.Or(linsets))
        return solver.check() == z3.sat
