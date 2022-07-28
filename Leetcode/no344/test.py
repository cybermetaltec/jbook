import unittest

from Leetcode.t import TestHelper
from Leetcode.no344 import Solution


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([["h", "e", "l", "l", "o"]], ["o", "l", "l", "e", "h"]),
            ([["H", "a", "n", "n", "a", "h"]], ["h", "a", "n", "n", "a", "H"]),
        ]
        self.test_template(cases, Solution, "reverseString", "assertEqual")


if __name__ == '__main__':
    unittest.main()
