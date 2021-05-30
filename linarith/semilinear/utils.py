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


def getGenerators(A, C):
    """
    Computes Hilbert basis of the system Ax <= 0 and Cx= 0, i.e. the basis
    of (A | I)(x) = (0)
       (C | 0)(y) = (0)
    """
    if A is None:
        m = len(C)
        n = len(C[0])
        generator_bound = int((n * oneInftyNorm(C) + 1) ** m)
        return hilbertBasis(C, generator_bound)

    m = len(A)
    n = len(A[0])
    A_ext = A.copy()
    A_ext = np.append(A_ext, np.identity(m), axis=1)
    print("A extended\n" + str(A_ext))
    if C is not None:
        mc = len(C)
        C_ext = C.copy()
        C_ext = np.append(C_ext, np.zeros((mc, mc)), axis=1)
        A_ext = np.stack(A_ext, C_ext)
        print("stacked: " + str(A_ext))
    generator_bound = int((n * oneInftyNorm(A_ext) + 1) ** m)

    # get a z3 solver instance and get bases
    solver, vrs = solverFromEquation(A_ext, np.zeros((len(A_ext),), dtype=int),
                                     generator_bound)
    no_zero = []
    for i in range(len(A_ext[0])):
        if i < n:
            no_zero.append(vrs[i] != 0)
        else:
            solver.add(vrs[i] >= 0)
    solver.add(z3.Or(no_zero))
    return getSolutions(solver, vrs)


def getBases(A, b, C, d):
    """
    Computes all bases of Ax=b and Cx=d, using the Hilbert basis
    of (A | -b)x = 0 and (C | -d)x = 0
    """
    if A is None:
        C_ext = np.append(C, np.array([-d]).transpose(), axis=1)
        m = len(C_ext)
        n = len(C_ext[0])
        generator_bound = int((n * oneInftyNorm(C_ext) + 1) ** m)
        return hilbertBasis(C_ext, generator_bound)

    if np.all(b == 0):
        return [np.zeros((len(A[0]),), dtype=int)]

    A_ext = A.copy()
    A_ext = np.append(A_ext, np.array([-b]).transpose(), axis=1)
    print("A extended\n" + str(A_ext))
    if C is not None:
        C_ext = C.copy()
        C_ext = np.append(C_ext, np.array([-d]).transpose(), axis=1)
        A_ext = np.stack(A_ext, C_ext)
        print("stacked: " + str(A_ext))

    m = len(A_ext)
    n = len(A_ext[0])

    # TODO: check bound
    base_bound = int((n * oneInftyNorm(A_ext) + 1) ** m)
    print("Extended for bases\n" + str(A_ext))

    # get a z3 solver instance and get the bases
    solver, vrs = solverFromEquation(A_ext, np.zeros((n,), dtype=int),
                                     base_bound)
    out = []
    no_zero = []
    # the last variable can only be 1, the other are nonzero
    for i in range(n - 1):
        no_zero.append(vrs[i] != 0)
    solver.add(vrs[n - 1] == 1)
    solver.add(z3.Or(no_zero))
    bases = getSolutions(solver, vrs)
    out = []
    for base in bases:
        out.append(np.array([base[i] for i in range(n - 1)]))
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
    no_zero = []
    for var in vrs:
        no_zero.append(var != 0)
    solver.add(z3.Or(no_zero))
    return getSolutions(solver, vrs)


def getSolutions(solver, vrs):
    out = []
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
