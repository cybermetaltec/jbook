from typing import List


# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix: return 0
#         m, n = len(matrix), len(matrix[0])
#         if m * n == 0: return 0
#         dp = [[0] * n for _ in range(m)]
#         Max = 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == "1":
#                     dp[i][j] = 1
#                     if j > 0: dp[i][j] += dp[i][j - 1]
#                     width = dp[i][j]
#                     for k in range(i, -1, -1):
#                         width = min(width, dp[k][j])
#                         if not width: break
#                         Max = max(Max, width * (i - k + 1))
#         return Max

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        if m * n == 0: return 0
        dp = [[0] * n for _ in range(m)]
        Max = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if j > 0: dp[i][j] += dp[i][j - 1]
                    width = dp[i][j]

        for j in range(n):
            stuck = []
            heights = [0] + [dp[i][j] for i in range(m)] + [0]
            for i, v in enumerate(heights):
                while stuck and v < heights[stuck[-1]]:
                    index = stuck.pop()
                    area = (i - stuck[-1] - 1) * heights[index]
                    Max = max(Max, area)
                stuck.append(i)
        return Max
