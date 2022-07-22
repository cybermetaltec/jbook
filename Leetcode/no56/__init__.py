from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        cur = intervals[0]
        ret = []
        for i in range(1, len(intervals)):
            a, b = cur
            c, d = intervals[i]
            if c > b:
                ret.append(cur)
                cur = intervals[i]
            else:
                cur = [a, max(b, d)]
        ret.append(cur)
        return ret
