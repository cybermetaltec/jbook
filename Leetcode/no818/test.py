import unittest

from Leetcode.t import TestHelper
from Leetcode.no818 import Solution


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([5399], 45),
            ([2045], 16),
            ([2794], 40),
            ([2333], 28),
            ([5], 7),
            ([20], 12),
            ([10], 7),
            ([6], 5),
            ([3], 2),
        ]
        self.test_template(cases, Solution, "racecar", "assertEqual")


if __name__ == '__main__':
    unittest.main()
