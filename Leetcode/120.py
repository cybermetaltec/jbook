from typing import List

from Leetcode.t import asrt


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        if row == 1: return triangle[0][0]
        for i in range(row - 2, -1, - 1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


asrt(Solution, "minimumTotal", [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]], 11)
asrt(Solution, "minimumTotal",  [[[-10]]], -10)
