from typing import List


class Solution:
    def __init__(self):
        self.n = None
        self.mod = None
        self.ret = 0

    def dfs(self, row, left, right, index):
        n = self.n
        if index == n:
            self.ret += 1
            return
        pos = ~(row | left | right) & self.mod
        while pos:
            lowest_1 = pos & -pos
            lowest_1_index = bin(lowest_1).count("0") - 1
            new_row = row + lowest_1
            new_left = (lowest_1 + left) << 1
            new_right = (lowest_1 + right) >> 1
            pos = pos ^ lowest_1
            self.dfs(new_row, new_left, new_right, index + 1)

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.mod = (1 << n) - 1
        self.dfs(0, 0, 0, 0)
        return self.ret
