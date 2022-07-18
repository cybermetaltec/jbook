import unittest
from Leetcode.no51 import Solution


class MyTestCase(unittest.TestCase):
    def test_solveNQueens(self):
        cases = [
            (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
            (1, [["Q"]])
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().solveNQueens(case)
                self.assertCountEqual(ret, ans, f'{ret} is not {ans}')


if __name__ == '__main__':
    unittest.main()
