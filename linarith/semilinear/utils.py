"""
Copyright 2020, 2021 Tim Leys
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

import numpy as np
import z3


def fromSystemIneqs(A, b):
    """
    Computes the semilinear set of solutions solutions of a set of linear
    diophantine inequalities  Ax <= b.
    :param A: The coefficient matrix of Ax <= b.
    :param b: The constant vector of Ax <= b.
    :return: A tuple of the bases and the generators (both as a list of numpy
    arrays).
    """
    m = len(A)
    n = len(A[0])
    print(str("m = " + str(m) + " n = " + str(n)))
    A_ext = A.copy()
    A_ext = np.append(A_ext, -1 * np.identity(m), axis=1)
    print(str(A_ext))
    generators = getGenerators(A_ext)
    bases = getBases(A_ext, b)
    generators_out = []
    bases_out = []
    for g in generators:
        generators_out.append(g[:n])
    for b in bases:
        bases_out.append(b[:n])
    return bases_out, minAntichain(generators_out)


def inftyNorm(v):
    """
    Computes the infinity norm of a vector. This maximum absolute value of the
    vector (or the 1-infinity norm of a 1 x m matrix).
    :param v: a flat numpy array
    :return: the infinity norm of v
    """
    temp = [abs(x) for x in v]
    return max(temp)


def oneInftyNorm(A):
    """
    Computes the 1-infinity norm of a matrix. The 1-infinity norm is the
    maximal sum of absolute values of a row.
    :param A: a numpy array matrix
    :return: the 1-infinity norm of A
    """
    temp = []
    for row in A:
        absrow = [abs(x) for x in row]
        temp.append(sum(absrow))
    return max(temp)


def getGenerators(A):
    """
    Computes Hilbert basis of the system Ax = 0.
    :param A: The coefficient matrix of Ax=0.
    :return: A set of generators for the semilinear set of solutions of Ax=0.
    """
    m = len(A)
    n = len(A[0])
    generator_bound = int((n * oneInftyNorm(A) + 1) ** m)
    return hilbertBasis(A, generator_bound)


def getBases(A, b):
    """
    Computes all bases of Ax=b, using the Hilbert basis of (A, -b)x = 0.
    :param A: The coefficient matrix of Ax = b.
    :param b: The constant vector of Ax=b.
    :return: A set of bases of the semilinear set of solutions for Ax=b.
    """
    m = len(A)
    n = len(A[0])
    if np.all(b == 0):
        return [np.zeros((n,), dtype=int)]
    base_bound = int(((n + 1) * oneInftyNorm(A) + inftyNorm(b) + 1) ** m)
    A_ext = np.append(A, np.array([-b]).transpose(), axis=1)
    print(str(A_ext))
    possible_bases = hilbertBasis(A_ext, base_bound)
    bases = [sol for sol in possible_bases if sol[n] == 1]
    out = []
    for base in bases:
        out.append(np.array([base[i] for i in range(n)]))
    return out


def hilbertBasis(A, abs_bound=0, positive=False):
    """
    Computes the Hilbert basis of Ax = 0. An absolute value bound can be
    enforced, as well as that the solutions are positive.
    :param A: The coefficient matrix of Ax = 0
    :param abs_bound: The bound of the absolute values of the solutions.
    :param positive: A boolean value to enforce only positive solutions or not.
    :return: The Hilbert basis of the solutions of Ax=0
    """
    solver, vrs = solverFromEquation(A, np.zeros((len(A),), dtype=int),
                                     abs_bound, positive)
    out = []
    no_zero = []
    for var in vrs:
        no_zero.append(var != 0)
    solver.add(z3.Or(no_zero))

    while solver.check() == z3.sat:
        out.append(solver.model())
        respect_order = []
        # add assertion to respect the order and avoid
        # repeated ones:
        # if u <= v, v is not in the Hilbert basis
        for v in vrs:
            if solver.model()[v].as_long() >= 0:
                respect_order.append(v < abs(solver.model()[v].as_long()))
            else:
                respect_order.append(v > -abs(solver.model()[v].as_long()))
        solver.add(z3.Or(respect_order))

    return minAntichain([toNparray(x) for x in out])


def solverFromEquation(A, b, abs_bound=0, positive=False):
    """
    Creates a z3 solver object with the assertions from the system of linear
    equations Ax=b.
    :param A: The coefficient matrix of Ax=b.
    :param b: The solution vector of Ax=b.
    :return: a tuple of the z3 zolver and a list of all variables.
    """
    m = len(A)
    n = len(A[0])
    vrs = [z3.Int("x%i" % i) for i in range(n)]
    print(str(vrs))
    solver = z3.Solver()
    for i in range(m):
        term = sum([A[i][j] * vrs[j] for j in range(n)])
        term = term == int(b[i])
        solver.add(term)
    if abs_bound != 0:
        for i in range(n):
            solver.add(vrs[i] < abs_bound)
            solver.add(vrs[i] > -abs_bound)
    if positive:
        for i in range(n):
            solver.add(vrs[i] >= 0)
    return solver, vrs


def toNparray(s):
    """
    Translate a z3 solution to a numpy array.
    :param s: A solution model of a z3 solver.
    :return: A numpy array with the valuation of the solution.
    """
    out = []
    vrs = [z3.Int("x%i" % i) for i in range(len(s))]
    for v in vrs:
        out.append(s[v].as_long())
    print(str(out))
    return np.array(out)


def minAntichain(bases):
    b = bases.copy()
    index = 0
    while index < len(b):
        if len(b) <= 1:
            return b
        v = b[index]
        other = b[:index] + b[index + 1:]
        if any(map(lambda x: dominated(v, x), other)):
            b = other
        else:
            index += 1
    return b


def dominated(v1, v2):
    for i in range(len(v1)):
        if v1[i] >= 0 and v2[i] < 0:
            return False
        if v2[i] >= 0 and v1[i] < 0:
            return False
        if abs(v1[i]) > abs(v2[i]):
            return False
    return True
