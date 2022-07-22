import unittest

from Leetcode.t import TestHelper
from Leetcode.no493 import Solution, case


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([[1, 3, 2, 3, 1]], 2),
            ([[2, 4, 3, 5, 1]], 3),
            ([case], 622550657),
        ]
        self.test_template(cases, Solution, "reversePairs", "assertEqual")


if __name__ == '__main__':
    unittest.main()
