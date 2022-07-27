import unittest
from Leetcode.no771 import Solution
from Leetcode.t import TestHelper


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            (["aA", "aAAbbbb"], 3),
            (["z", "ZZ"], 0),
        ]
        self.test_template(cases, Solution, "numJewelsInStones", "assertEqual")


if __name__ == '__main__':
    unittest.main()
