from typing import List

from Leetcode.t import asrt


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp_in = prices[:]
#         dp_out = dp_in[:]
#         dp_out[0] = MAX = 0
#         for i in range(1, len(prices)):
#             dp_in[i] = min(dp_in[i - 1], prices[i])
#             dp_out[i] = prices[i] - dp_in[i]
#             MAX = max(dp_out[i], MAX)
#         return MAX

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = [[0] * len(prices) for _ in range(2)]
#         dp[1][0] = prices[0]
#         MAX = 0
#         for i in range(1, len(prices)):
#             dp[1][i] = min(dp[1][i - 1], prices[i])
#             dp[0][i] = prices[i] - dp[1][i]
#             MAX = max(dp[0][i], MAX)
#         return MAX

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         lowest, MAX = prices[0], 0
#         for price in prices:
#             lowest = min(price, lowest)
#             MAX = max(MAX, price - lowest)
#         return MAX


asrt(Solution, "maxProfit", [[7, 1, 5, 3, 6, 4]], 5)
asrt(Solution, "maxProfit", [[7, 6, 4, 3, 1]], 0)
