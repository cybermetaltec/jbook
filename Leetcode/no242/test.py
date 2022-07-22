import unittest
from Leetcode.no242 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cases = [
            (["anagram", "nagaram"], True),
            (["rat", "car"], False),
        ]
        for case, ans in cases:
            with self.subTest(case):
                ret = Solution().isAnagram(*case)
                self.assertEqual(ret, ans, f"case:{case},ret:{ret},ans:{ans}")

if __name__ == '__main__':
    unittest.main()
