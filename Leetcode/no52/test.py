import unittest
from Leetcode.no52 import Solution


class MyTestCase(unittest.TestCase):
    def test_solveNQueens(self):
        cases = [
            (4, 2),
            (1, 1),
            (8, 92),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().totalNQueens(case)
                self.assertEqual(ret, ans, f'{ret} is not {ans}')


if __name__ == '__main__':
    unittest.main()
