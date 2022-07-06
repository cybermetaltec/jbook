from typing import List

from Leetcode.t import asrt


# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         row, col, max_area = len(matrix), len(matrix[0]), 0
#         for r in range(0, row):
#             for c in range(0, col):
#                 if matrix[r][c] == "1":
#                     width = min(int(matrix[r - 1][c]), int(matrix[r][c - 1]),
#                                 int(matrix[r - 1][c - 1])) + 1 if r * c else 1
#                     max_area = max(max_area, width ** 2)
#                     matrix[r][c] = str(width)
#
#         return max_area


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = {}

        def get_width(tmp):
            if tmp in m: return m[tmp]
            n, t = 0, tmp
            while t:
                t &= t << 1
                n += 1
            m[tmp] = n
            return n

        max_area = 0
        row_nums = [int("".join(i), 2) for i in matrix]
        for i, v in enumerate(row_nums):
            tmp = v
            for i2, v2 in enumerate(row_nums[i:]):
                tmp &= v2
                width = get_width(tmp)
                height = i2 + 1
                if width * height: max_area = max(max_area, min(width, height) ** 2)
        return max_area


asrt(Solution, "maximalSquare",
     [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], 4)
asrt(Solution, "maximalSquare",
     [[["0", "1"], ["1", "0"]]], 1)
asrt(Solution, "maximalSquare",
     [[["0"], ["1"]]], 1)
asrt(Solution, "maximalSquare",
     [[["0"]]], 0)
asrt(Solution, "maximalSquare",
     [[["1"]]], 1)
asrt(Solution, "maximalSquare",
     [[["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1"],
       ["1", "1", "1", "1", "1"]]], 4)
