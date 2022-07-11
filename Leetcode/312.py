from typing import List

from Leetcode.t import asrt


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for high in range(2, n):
            for low in range(high - 2, -1, -1):
                for k in range(low + 1, high):
                    ret = nums[low] * nums[k] * nums[high] + dp[low][k] + dp[k][high]
                    dp[low][high] = max(dp[low][high], ret)
        return dp[0][-1]


asrt(Solution, "maxCoins", [[3, 1, 5, 8]], 167)
asrt(Solution, "maxCoins", [[1, 5]], 10)
asrt(Solution, "maxCoins", [[1]], 1)
asrt(Solution, "maxCoins", [[5]], 5)
