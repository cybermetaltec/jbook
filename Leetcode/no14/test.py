import unittest

from Leetcode.t import TestHelper
from Leetcode.no14 import Solution


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            ([["flower", "flow", "flight"]], "fl"),
            ([["d", "dg", "dgg"]], "d"),
            ([["dg", "dg", "dgg"]], "dg"),
            ([["dog", "racecar", "car"]], ""),
            ([["", "racecar", "car"]], ""),
            ([["asd", "", "as"]], ""),
        ]
        self.test_template(cases, Solution, "longestCommonPrefix", "assertEqual")


if __name__ == '__main__':
    unittest.main()
