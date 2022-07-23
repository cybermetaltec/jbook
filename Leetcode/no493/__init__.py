from collections import deque
from typing import List, Deque
from Leetcode.no493.case import case
from sortedcontainers import SortedList


# class Solution:
#     def __init__(self):
#         self.count = 0
#
#     def get_reverse_count(self, l1: List[int], l2: List[int]) -> None:
#         i = j = 0
#         while i < len(l1) and j < len(l2):
#             if l1[i] > 2 * l2[j]:
#                 self.count += len(l1) - i
#                 j += 1
#             else:
#                 i += 1
#
#     def _merge(self, l1: Deque[int], l2: Deque[int]):
#         while l1 and l2:
#             yield (l1 if l1[0] < l2[0] else l2).popleft()
#         yield from l1
#         yield from l2
#
#     def merge(self, l1: List[int], l2: List[int]) -> List[int]:
#         self.get_reverse_count(l1, l2)
#         return list(self._merge(deque(l1), deque(l2)))
#
#     def merge_sort(self, nums: List[int]) -> List[int]:
#         if len(nums) <= 1: return nums
#         mid = len(nums) >> 1
#         l1 = self.merge_sort(nums[:mid])
#         l2 = self.merge_sort(nums[mid:])
#         return self.merge(l1, l2)
#
#     def reversePairs(self, nums: List[int]) -> int:
#         self.merge_sort(nums)
#         return self.count

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ret, l = 0, SortedList()
        for num in nums:
            i = l.bisect_right(2 * num)
            ret += len(l) - i
            l.add(num)
        return ret
