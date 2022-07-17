import unittest
from Leetcode.no191 import Solution


class MyTestCase(unittest.TestCase):
    def test_hammingWeight(self):
        cases = [
            (0b00000000000000000000000000001011, 3),
            (0b00000000000000000000000010000000, 1),
            (0b11111111111111111111111111111101, 31),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().hammingWeight(case)
                self.assertEqual(ret, ans, f"{ret} is not {ans}")


if __name__ == '__main__':
    unittest.main()
