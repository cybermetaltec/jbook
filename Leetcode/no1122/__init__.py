import collections
from typing import List


class Solution0:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count, others, m = [0] * len(arr2), [], {v: i for i, v in enumerate(arr2)}
        for num in arr1:
            if (index := m.get(num, None)) is not None:
                count[index] += 1
            else:
                others.append(num)

        ret = [i for num, n in zip(arr2, count) for i in [num] * n] + sorted(others)
        return ret


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        others, m = [], collections.OrderedDict({v: 0 for v in arr2})
        for num in arr1:
            if num in m:
                m[num] += 1
            else:
                others.append(num)

        ret = [i for num, n in m.items() for i in [num] * n] + sorted(others)
        return ret
