import unittest

from Leetcode.n773 import Solution


class SolutionTest(unittest.TestCase):
    def test_slidingPuzzle(self):
        cases = [
            ([[1, 2, 3], [4, 0, 5]], 1),
            ([[4, 1, 2], [5, 0, 3]], 5),
            ([[1, 2, 3], [5, 4, 0]], -1)
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().slidingPuzzle(case)
                self.assertEqual(ret, ans)

    def test_have_ans(self):
        cases = [
            ("123405", True),
            ("412503", True),
            ("123540", False)
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().have_ans(case)
                self.assertEqual(ret, ans, case)


if __name__ == '__main__':
    unittest.main()
