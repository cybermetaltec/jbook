from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ret = deque(), []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# size = 3

nums = [1,-1]
size = 1
print(Solution().maxSlidingWindow(nums, size))
