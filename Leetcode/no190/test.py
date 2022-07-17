import unittest
from Leetcode.no190 import Solution


class MyTestCase(unittest.TestCase):
    def test_reverseBits(self):
        cases = [
            (0b00000010100101000001111010011100, 964176192),
            (0b11111111111111111111111111111101, 3221225471),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().reverseBits(case)
                self.assertEqual(ret, ans, f'{bin(ret)} is not {bin(ans)}')


if __name__ == '__main__':
    unittest.main()
