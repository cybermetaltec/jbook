from typing import List


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         b = [0] * n
#         mod = (1 << n) - 1
#         stuck = [(0, 0, 0, [])]
#         ret = []
#         while stuck:
#             row, left, right, ans = stuck.pop()
#             if len(ans) == n:
#                 ret.append(ans)
#                 continue
#             pos = ~(row | left | right) & mod
#             while pos:
#                 s = ["."] * n
#                 lowest_1 = pos & -pos
#                 lowest_1_index = bin(lowest_1).count("0") - 1
#                 s[lowest_1_index] = "Q"
# 
#                 new_row = row | (1 << (n - lowest_1_index - 1))
#                 new_left = (new_row + left) << 1
#                 new_right = (new_row + right) >> 1
#                 stuck.append((new_row, new_left, new_right, ans + ["".join(s)]))
#                 pos = pos ^ lowest_1
#         return ret

class Solution:
    def __init__(self):
        self.n = None
        self.mod = None
        self.ret = []

    def dfs(self, row, left, right, data):
        n = self.n
        if len(data) == n:
            self.ret.append(data)
            return
        pos = ~(row | left | right) & self.mod
        while pos:
            s = ["."] * n
            lowest_1 = pos & -pos
            lowest_1_index = bin(lowest_1).count("0") - 1
            s[n - lowest_1_index - 1] = "Q"
            new_row = row + lowest_1
            new_left = (lowest_1 + left) << 1
            new_right = (lowest_1 + right) >> 1
            pos = pos ^ lowest_1
            self.dfs(new_row, new_left, new_right, data + ["".join(s)])

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.mod = (1 << n) - 1
        self.dfs(0, 0, 0, [])
        return self.ret
