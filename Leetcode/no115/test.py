import unittest

from Leetcode.t import TestHelper
from Leetcode.no115 import Solution


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            (["rabbbit", "rabbit"], 3),
            (["babgbag", "bag"], 5),
            (["", "bag"], 0),
            (["babgbag", ""], 1),
        ]
        self.test_template(cases, Solution, "numDistinct", "assertEqual")


if __name__ == '__main__':
    unittest.main()
