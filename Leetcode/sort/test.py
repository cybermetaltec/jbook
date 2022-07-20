import random
import unittest

from Leetcode.sort import QuikSort, MergeSort


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.case = [random.randint(0, 100) for _ in range(99)]

    def test_quick_sort(self):
        cp1 = self.case[:]
        cp2 = self.case[:]
        QuikSort().sort(cp1)
        ans = sorted(cp2)
        self.assertEqual(cp1, ans)  # add assertion here

    def test_merge_sort(self):
        cp1 = self.case[:]
        cp2 = self.case[:]
        ret = MergeSort().sort(cp1)
        ans = sorted(cp2)
        self.assertEqual(ret, ans)  # add assertion here

    def test_heap_sort(self):
        cp1 = self.case[:]
        cp2 = self.case[:]
        quick_sort(cp1)
        ans = sorted(cp2)
        self.assertListEqual(cp1, cp2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
