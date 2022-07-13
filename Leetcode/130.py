import math
from typing import List
from Leetcode.UnionSet import UnionSet


# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         m, n = len(board), len(board[0])
#         if m * n <= 4: return
#         for i in range(m):
#             check = range(n)
#             if i not in (0, m - 1): check = [0, n - 1]
#             for j in check:
#                 if board[i][j] == "O":
#                     for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#                         if 1 <= x < m - 1 and 1 <= y < n - 1 and board[x][y] == "O":
#                             self.dfs(x, y, board, "#", "O")
#
#         for i in range(1, m - 1):
#             for j in range(1, n - 1):
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 if board[i][j] == "#":
#                     board[i][j] = "O"
#
#     def dfs(self, i, j, board, tag, condition):
#         m, n = len(board), len(board[0])
#         board[i][j] = tag
#         for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#             if 1 <= x < m - 1 and 1 <= y < n - 1 and board[x][y] == condition:
#                 self.dfs(x, y, board, tag, condition)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        if m * n <= 4: return
        p = [i for i in range(m * n + 1)]
        us = UnionSet(p, len(p))
        us.rank[-1] = math.inf

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i in (0, m - 1) or j in [0, n - 1]:
                        us.union(i * n + j, m * n)
                    else:
                        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                                us.union(i * n + j, x * n + y)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O" and us.find(p[i * n + j]) != p[-1]:
                    board[i][j] = "X"



board = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O", "O", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "O", "O", "O", "X", "O", "X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "O", "X", "O", "X", "O", "X", "O", "O", "O", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "O", "X", "O", "O", "O", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "O", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
]

Solution().solve(board)
print(board)
# board = [
#     ["O", "O", "O", "O", "X", "X"],
#     ["O", "O", "O", "O", "O", "O"],
#     ["O", "X", "O", "X", "O", "O"],
#     ["O", "X", "O", "O", "X", "O"],
#     ["O", "X", "O", "X", "O", "O"],
#     ["O", "X", "O", "O", "O", "O"]
# ]
#
# Solution().solve(board)
# print(board)
#
# board = [
#     ["X", "X", "X", "X", "X"],
#     ["X", "O", "X", "O", "X"],
#     ["X", "O", "X", "O", "X"],
#     ["X", "O", "X", "O", "X"],
#     ["X", "O", "X", "X", "X"]
# ]
# Solution().solve(board)
# print(board)
#
# board = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"]
# ]
# Solution().solve(board)
# print(board)
#
# board = [["X"]]
# Solution().solve(board)
# print(board)
#
# board = [["O"]]
# Solution().solve(board)
# print(board)
