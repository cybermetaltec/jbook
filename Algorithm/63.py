from typing import List

from Algorithm.t import asrt


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        i, dp[0][0] = 0, 1
        while i < m * n:
            m1, n1 = i // n, i % n
            if obstacleGrid[m1][n1] == 0:
                if m - 1: dp[m1][n1] += dp[m1 - 1][n1]
                if n - 1: dp[m1][n1] += dp[m1][n1 - 1]
            else:
                dp[m1][n1] = 0
            i += 1
        return dp[m - 1][n - 1]


asrt(Solution, "uniquePathsWithObstacles", [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], 2)
asrt(Solution, "uniquePathsWithObstacles", [[[0, 1], [0, 0]]], 1)
asrt(Solution, "uniquePathsWithObstacles", [[[1]]], 0)
