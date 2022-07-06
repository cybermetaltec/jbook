from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         count, money = 0, 0
#         for i in range(len(prices)):
#             today = prices[i]
#             tomorrow = prices[i + 1] if i + 1 < len(prices) else None
#
#             if not count and tomorrow is not None and tomorrow > today:
#                 count = 1
#                 money -= today
#             if count and (tomorrow is None or tomorrow < today):
#                 count = 0
#                 money += today
#
#         return money

# 动态规划

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in prices]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


pricess = [7, 1, 5, 3, 6, 4]
ret = Solution().maxProfit(pricess)
assert ret == 7, f'{ret} is not 7'

pricess = [1, 2, 3, 4, 5]
ret = Solution().maxProfit(pricess)
assert ret == 4, f'{ret} is not 4'

pricess = [7, 1, 5, 3, 6, 4]
ret = Solution().maxProfit(pricess)
assert ret == 7, f'{ret} is not 7'

pricess = [7, 6, 4, 3, 1]
ret = Solution().maxProfit(pricess)
assert ret == 0, f'{ret} is not 0'
