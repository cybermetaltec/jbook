from collections import Counter
from typing import List

from Leetcode.t import asrt


# 遍历
class Solution0:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows, cols = {r: Counter() for r in range(m)}, {c: Counter() for c in range(m)}
        box = {b: Counter() for b in range(m)}
        for i in range(m):
            for j in range(n):
                num = board[i][j]
                if num == ".": continue
                rows[i][num] += 1
                cols[j][num] += 1
                box_i, box_j = i // 3, j // 3
                box_index = box_i * 3 + box_j
                box[box_index][num] += 1
                if rows[i][num] > 1 or cols[j][num] > 1 or box[box_index][num] > 1:
                    return False
        return True


# 二进制
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, box = [0] * 9, [0] * 9, [0] * 9
        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == ".": continue
                num = int(s)
                num_exist_row = rows[i] >> num & 1
                num_exist_col = cols[j] >> num & 1
                box_i, box_j = i // 3, j // 3
                box_index = box_i * 3 + box_j
                num_exist_box = box[box_index] >> num & 1
                if 1 in {num_exist_row, num_exist_col, num_exist_box}: return False
                num_b = 1 << num
                rows[i] ^= num_b
                cols[j] ^= num_b
                box[box_index] ^= num_b
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
asrt(Solution, "isValidSudoku", [board], True)
board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

asrt(Solution, "isValidSudoku", [board], False)

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
asrt(Solution, "isValidSudoku", [board], False)
