import math
from functools import reduce
from typing import List

from Leetcode.t import asrt


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        head_row = [grid[0][:1] + [i for i in map(lambda i: reduce(lambda x, y: x + y, grid[0][:i + 1]), range(1, n))]]
        dp = head_row + [[sum([grid[j][0] for j in range(i + 1)])] + grid[i][1:] for i in range(1, m)]
        total = m * n
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


asrt(Solution, "minPathSum", [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]], 7)
asrt(Solution, "minPathSum", [[[1, 2, 3], [4, 5, 6]]], 12)
asrt(Solution, "minPathSum", [[[1]]], 1)
asrt(Solution, "minPathSum", [[[1, 3]]], 4)
asrt(Solution, "minPathSum", [[[1], [3]]], 4)
