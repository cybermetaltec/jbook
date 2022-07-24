import unittest

from Leetcode.t import TestHelper
from Leetcode.no85 import Solution

m1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]]
m2 = [
    ["1", "0", "1", "1", "1"],
    ["0", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "1"],
    ["1", "1", "0", "1", "1"],
    ["0", "1", "1", "1", "1"]
]


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([m2], 6),
            ([m1], 6),
            ([[]], 0),
            ([[["0"]]], 0),
            ([[["1"]]], 1),
        ]
        self.test_template(cases, Solution, "maximalRectangle", "assertEqual")


if __name__ == '__main__':
    unittest.main()
