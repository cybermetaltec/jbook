import unittest
from Leetcode.no56 import Solution


class MyTestCase(unittest.TestCase):
    def test_merge(self):
        cases = [
            ([[1, 5], [5, 6], [6, 10], [15, 18]], [[1, 10], [15, 18]]),
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),
            ([[2, 3]], [[2, 3]]),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().merge(case)
                self.assertCountEqual(ret, ans, f"case:{case},ret:{ret},ans:{ans}")


if __name__ == '__main__':
    unittest.main()
