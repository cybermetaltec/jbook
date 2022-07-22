import unittest
from Leetcode.no1122 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cases = [
            ([[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]], [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
            ([[28, 6, 22, 8, 44, 17], [22, 28, 8, 6]], [22, 28, 8, 6, 17, 44]),
        ]

        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().relativeSortArray(*case)
                self.assertEqual(ret, ans, f'case:{case},ret:{ret},answer:{ans}')


if __name__ == '__main__':
    unittest.main()
