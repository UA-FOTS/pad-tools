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

import numpy as np
import unittest

from linarith.semilinear.HyLinSet import HyLinSet


class SemilinearTests(unittest.TestCase):
    def testAb1(self):
        A = np.array([[4, 1],
                      [2, 2]])
        b = np.array([0, 0]).transpose()
        slset = HyLinSet(A, b)
        self.assertTrue(np.array([0, 0]).transpose() in slset)
        self.assertFalse(np.array([1, 1]).transpose() in slset)
        self.assertTrue(np.array([-1, 1]).transpose() in slset)
        self.assertFalse(np.array([1, -1]).transpose() in slset)
        self.assertTrue(np.array([-10, -10]).transpose() in slset)
        self.assertTrue(np.array([10, -100]).transpose() in slset)

    def testCd1(self):
        C = np.array([[4, 1],
                      [2, 2]])
        d = np.array([0, 0]).transpose()
        slset = HyLinSet(None, None, C, d)
        self.assertTrue(np.array([0, 0]).transpose() in slset)
        self.assertFalse(np.array([-1, 1]).transpose() in slset)


if __name__ == '__main__':
    unittest.main()
