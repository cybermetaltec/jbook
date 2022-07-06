from typing import List

from Leetcode.t import asrt


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i - 1], nums[i])
            ret = max(ret, nums[i])
        return ret


asrt(Solution, "maxSubArray", [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 6)
asrt(Solution, "maxSubArray", [[1]], 1)
asrt(Solution, "maxSubArray", [[5, 4, -1, 7, 8]], 23)
