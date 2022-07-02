from typing import List

from Algorithm.t import asrt


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:return nums[0]
        dp = nums[:]
        dp[1] = max(dp[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + dp[i], dp[i - 1])
        return dp[-1]


asrt(Solution, "rob", [[2, 1, 1, 2]], 4)
asrt(Solution, "rob", [[1, 2, 3, 1]], 4)
asrt(Solution, "rob", [[2, 7, 9, 3, 1]], 12)
asrt(Solution, "rob", [[2]], 2)
asrt(Solution, "rob", [[2, 3]], 3)
asrt(Solution, "rob", [[3, 2]], 3)
