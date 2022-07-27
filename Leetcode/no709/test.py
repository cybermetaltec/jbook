import random
import unittest

from Leetcode.t import TestHelper
from Leetcode.no709 import Solution


def gen_case():
    return "".join([chr(random.randint(32, 128)) for _ in range(100)])


class MyTestCase(TestHelper):
    def test_something(self):
        strs = [gen_case() for _ in range(100)]
        cases = [([s], s.lower()) for s in strs]
        self.test_template(cases, Solution, "toLowerCase", "assertEqual")


if __name__ == '__main__':
    unittest.main()
