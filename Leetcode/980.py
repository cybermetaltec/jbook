from typing import List

from Leetcode.t import asrt


class Solution:
    ans = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def get_data(matrix):
            start, end, blanks = [0, 0], [0, 0], 0
            for row, v_row in enumerate(grid):
                for col, v_col in enumerate(v_row):
                    if v_col == 1: start = [row, col]
                    if v_col == 2:
                        end = [row, col]
                        blanks += 1
                    if v_col == 0: blanks += 1
            return start, end, blanks

        def get_nei_bors(r, c):
            for y, x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= y < m and 0 <= x < n and grid[y][x] in {2, 0}: yield y, x

        def dfs(s, b):
            r, c = s
            if grid[r][c] == 2 and b == 1:
                self.ans += 1
                return
            if b == 0 or grid[r][c] == 2: return
            if grid[r][c] == 0: b -= 1
            grid[r][c] = -1
            nei_bors = get_nei_bors(*s)
            for r, c in nei_bors:
                tmp = grid[r][c]
                dfs((r, c), b)
                grid[r][c] = tmp

        m, n = len(grid), len(grid[0])
        start, end, blanks = get_data(grid)
        dfs(start, blanks)
        return self.ans


asrt(Solution, "uniquePathsIII", [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]], 2)
asrt(Solution, "uniquePathsIII", [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]], 4)
asrt(Solution, "uniquePathsIII", [[[0, 1], [2, 0]]], 0)
asrt(Solution, "uniquePathsIII", [[[1, 2]]], 1)
