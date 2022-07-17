from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        prev = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                dp[i] = 1
                prev = i
            else:
                dp[i] = 1 + dp[i - prev]
        return dp
