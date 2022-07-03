import math

from Algorithm.t import asrt


class Solution:
    def numSquares(self, n: int) -> int:
        options = math.isqrt(n)
        MAX = n + 1
        dp = [MAX] * (n + 1)
        dp[0] = 0
        for num in range(1, options + 1):
            coin = num * num
            for i in range(coin, n + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1]


asrt(Solution, "numSquares", [13], 2)
asrt(Solution, "numSquares", [12], 3)
asrt(Solution, "numSquares", [16], 1)
asrt(Solution, "numSquares", [1], 1)
