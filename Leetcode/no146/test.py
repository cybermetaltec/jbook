import unittest
from Leetcode.no146 import LRUCache


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cases = [
            (
                2,
                ["put", "put", "get", "put", "put", "get"],
                [[2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
                [None, None, 2, None, None, -1]
            ),
            (
                2,
                ["put", "put", "get", "put", "get", "put", "get", "get", "get"],
                [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                [None, None, 1, None, -1, None, -1, 3, 4]
            ),
            (
                1,
                ["put", "get", "put", "get", "get"],
                [[2, 1], [2], [3, 2], [2], [3]],
                [None, 1, None, -1, 2]
            )
        ]
        for case in cases:
            with self.subTest(case):
                size, act, params, ans = case
                lRUCache = LRUCache(size)
                for a, p, r in zip(act, params, ans):
                    fn = getattr(lRUCache, a)
                    ret = fn(*p)
                    self.assertEqual(ret, r, f'action:{a},params:{p},ret:{ret} is not answer:{r}')

    if __name__ == '__main__':
        unittest.main()
