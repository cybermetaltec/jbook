from typing import List

from Leetcode.t import asrt


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
            dp[i][2] = dp[i - 1][0]
        return dp[-1][0]


asrt(Solution, "maxProfit", [[1, 2, 3, 0, 2]], 3)
asrt(Solution, "maxProfit", [[1]], 0)
asrt(Solution, "maxProfit", [[6, 10, 0, 8, 8]], 8)
asrt(Solution, "maxProfit", [[6, 0, 6, 9, 5]], 9)
