import unittest
from Leetcode.no300 import Solution
from Leetcode.t import TestHelper


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([[10, 9, 2, 5, 3, 7, 101, 18]], 4),
            ([[0, 1, 0, 3, 2, 3]], 4),
            ([[0, 1, 2, 3, 2, 3]], 4),
            ([[7, 7, 7, 7, 7, 7, 7]], 1),
        ]
        self.test_template(cases, Solution, "lengthOfLIS", "assertEqual")


if __name__ == '__main__':
    unittest.main()
