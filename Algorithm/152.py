from typing import List

from Algorithm.t import asrt


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max, prev_min = nums[0], 1
        ret = nums[0]
        for i in range(1, len(nums)):
            child = [prev_max * nums[i], prev_min * nums[i], nums[i]]
            prev_max = max(child)
            prev_min = min(child)
            ret = max(ret, prev_max)

        return ret


asrt(Solution, "maxProduct", [[2, 3, -2, 4]], 6)
asrt(Solution, "maxProduct", [[-2, 0, -1]], 0)
asrt(Solution, "maxProduct", [[1]], 1)
