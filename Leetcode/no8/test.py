import unittest
from Leetcode.no8 import Solution
from Leetcode.t import TestHelper


class MyTestCase(TestHelper):
    def test_something(self):
        cases = [
            (["42"], 42),
            (["   -42"], -42),
            (["   -42   "], -42),
            (["4193 with words"], 4193),
            (["+4193 with words"], 4193),
            (["41+93 with words"], 41),
            (["41.931212 with words"], 41),
            (["  +41  93 with words"], 41),
            (["  0041  93 with words"], 41),
            (["  -0041  93 with words"], -41),
            ([" 4100 with words"], 4100),
            (["asdasfdasf asdasd"], 0),
            (["-2147483649d"], -2147483648),
            (["2147483648d"], 2147483647),
            (["asa2147483648d"], 0),
            (["words and 987"], 0),
            (["+-12"], 0),
            (["+0"], 0),
            (["+1"], 1),
            (["00000-42a1234"], 0),
        ]
        self.test_template(cases, Solution, "myAtoi", "assertEqual")


if __name__ == '__main__':
    unittest.main()
