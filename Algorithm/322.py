from typing import List

from Algorithm.t import asrt
from collections import deque


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not amount: return amount
#         q = deque([amount])
#         count = 0
#         visited = set()
#         while q:
#             for i in range(len(q)):
#                 num = q.popleft()
#                 for coin in coins:
#                     new_amount = num - coin
#                     if new_amount == 0: return count + 1
#                     if new_amount > 0 and new_amount not in visited:
#                         visited.add(new_amount)
#                         q.append(new_amount)
#             count += 1
#         return -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        dp = [0] + [MAX for _ in range(amount)]
        for coin in coins:
            for i in range(coin, MAX):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != MAX else -1


asrt(Solution, "coinChange", [[1, 2, 5], 11], 3)
asrt(Solution, "coinChange", [[2], 3], -1)
asrt(Solution, "coinChange", [[1], 0], 0)
asrt(Solution, "coinChange", [[186, 419, 83, 408], 6249], 20)
