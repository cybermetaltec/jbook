from Algorithm.t import asrt


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        i = 0
        while i < m * n:
            m1, n1 = i // n, i % n
            if m1: dp[m1][n1] += dp[m1 - 1][n1]
            if n1: dp[m1][n1] += dp[m1][n1 - 1]
            i += 1
        return dp[m - 1][n - 1]


asrt(Solution, "uniquePaths", [3, 7], 28)
asrt(Solution, "uniquePaths", [3, 3], 6)
