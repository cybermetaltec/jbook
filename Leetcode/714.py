from typing import List

from Leetcode.t import asrt


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]


asrt(Solution, "maxProfit", [[1, 3, 2, 8, 4, 9], 2], 8)
asrt(Solution, "maxProfit", [[1, 3, 7, 5, 10, 3], 3], 6)
