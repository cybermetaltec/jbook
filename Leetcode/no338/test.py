import unittest
from Leetcode.no338 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cases = [
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
            (9, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]),
            (20, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]),
            (100,
             [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2,
              3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3,
              3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3]),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().countBits(case)
                self.assertEqual(ret, ans, f'{ret} is not {ans}')


if __name__ == '__main__':
    unittest.main()
