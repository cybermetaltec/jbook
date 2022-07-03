from typing import List

from Algorithm.t import asrt


# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if not k or len(prices) < 2: return 0
#         dp = [[[0, 0] for _ in range(k)] for _ in range(len(prices))]
#         for i in range(k):
#             dp[0][i][1] = -prices[0]
#         for i in range(1, len(prices)):
#             for j in range(k):
#                 dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
#                 yesterday_sell = dp[i - 1][j - 1][0] if j else 0
#                 dp[i][j][1] = max(dp[i - 1][j][1], yesterday_sell - prices[i])
#         return max([j[0] for j in dp[-1] if j])

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or len(prices) < 2: return 0
        dp = [[0, -prices[0]] for _ in range(k)]
        for i in range(0, len(prices)):
            for j in range(k):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                prev_sell = dp[j - 1][0] if j else 0
                dp[j][1] = max(dp[j][1], prev_sell - prices[i])
        return dp[-1][0]


asrt(Solution, "maxProfit", [2, [3, 2, 6, 5, 0, 3]], 7)
asrt(Solution, "maxProfit", [2, [2, 4, 1]], 2)
asrt(Solution, "maxProfit", [0, [2, 4, 1]], 0)
asrt(Solution, "maxProfit", [2, []], 0)
asrt(Solution, "maxProfit", [2, [2]], 0)
asrt(Solution, "maxProfit", [2, [2, 3]], 1)
asrt(Solution, "maxProfit", [2, [3, 2]], 0)
asrt(Solution, "maxProfit", [2, [3, 3, 5, 0, 0, 3, 1, 4]], 6)
