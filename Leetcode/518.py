from typing import List

from Leetcode.t import asrt


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0] * (amount + 1) for _ in range(n + 1)]
#         dp[0][0] = 1
#         for i in range(1, n + 1):
#             for j in range(0, amount + 1):
#                 dp[i][j] = dp[i - 1][j]
#                 if j - coins[i - 1] >= 0: dp[i][j] += dp[i][j - coins[i - 1]]
#         return dp[-1][-1]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                if i - coin >= 0: dp[i] += dp[i - coin]
        return dp[amount]


asrt(Solution, "change", [5, [1, 2, 5]], 4)
asrt(Solution, "change", [3, [2]], 0)
