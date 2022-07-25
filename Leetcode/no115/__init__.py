class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s) + 1, len(t) + 1
        # dp[i][j]代表t的前i个字符在s的前j个字符中出现的次数
        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
