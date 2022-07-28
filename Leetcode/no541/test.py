import unittest

from Leetcode.t import TestHelper
from Leetcode.no541 import Solution


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            (["abcdefg", 2], "bacdfeg"),
            (["abcdefg", 1], "abcdefg"),
            (["abcdefgh", 2], "bacdfegh"),
            (["abcd", 2], "bacd"),
            (["abc", 2], "bac"),
            (["ab", 2], "ba"),
            (["a", 2], "a"),
            (["a", 1], "a"),
            (["abcde", 2], "bacde"),
            (["abcdef", 2], "bacdfe"),
        ]
        self.test_template(cases, Solution, "reverseStr", "assertEqual")


if __name__ == '__main__':
    unittest.main()
