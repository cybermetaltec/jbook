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
        p = [2 for i in range(m * n)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X": p[i * n + j] = 0
                if board[i][j] == "O":
                    if i in {0, m - 1} or j in {0, n - 1}:
                        p[i * n + j] = 2
                    else:
                        p[i * n + j] = 1
            # check = range(n)
            # if i not in (0, m - 1): check = [0, n - 1]
            # for j in check:
            #     if board[i][j] == "X": p[i * n + j] = 0
            #     if board[i][j] == "O": p[i * n + j] = 1
        # for i in range(1, m - 1):
        #     for j in range(1, n - 1):
        #         for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        #             if p[x * n + y] == 1: p[i * n + j] = 1
        #         if p[i * n + j] != 1 and board[i][j] == "O":
        #             board[i][j] = "X"

        print(p)


[0, 0, 0, 0, 0,
 0, 1, 0, 1, 0,
 0, 1, 0, 1, 0,
 0, 1, 0, 1, 0,
 0, 2, 0, 0, 0]
board = [
    ["X", "X", "X", "X", "X"],
    ["X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X"],
    ["X", "O", "X", "X", "X"]
]
Solution().solve(board)
print(board)

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
Solution().solve(board)
print(board)

board = [["X"]]
Solution().solve(board)
print(board)

board = [["O"]]
Solution().solve(board)
print(board)
