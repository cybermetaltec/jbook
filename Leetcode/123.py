from typing import List

from Leetcode.t import asrt


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0, 0], [0, 0]] for _ in range(len(prices))]
        dp[0][0][1] = dp[0][1][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1] + prices[i])
            dp[i][0][1] = max(dp[i - 1][0][1], -prices[i])

            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
        return max(dp[-1][0][0], dp[-1][1][0])


asrt(Solution, "maxProfit", [[3, 3, 5, 0, 0, 3, 1, 4]], 6)
asrt(Solution, "maxProfit", [[1, 2, 3, 4, 5]], 4)
asrt(Solution, "maxProfit", [[7, 6, 4, 3, 1]], 0)
asrt(Solution, "maxProfit", [[1]], 0)
