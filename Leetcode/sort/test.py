import random
import unittest
from typing import Callable, ClassVar

from Leetcode.sort import QuickSort, MergeSort


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [[random.randint(0, 100) for _ in range(random.randint(0, 100))] for _ in range(100)]

    def _test_sort(self, fn: ClassVar):
        for case in self.cases:
            ret = fn().sort(case[:])
            ans = sorted(case[:])
            self.assertEqual(ret, ans)

    def test_quick_sort(self):
        self._test_sort(QuickSort)

    def test_merge_sort(self):
        self._test_sort(MergeSort)

    def test_heap_sort(self):
        pass


if __name__ == '__main__':
    unittest.main()
