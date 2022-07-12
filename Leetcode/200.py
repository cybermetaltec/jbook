from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(r, c):
#             grid[r][c] = "0"
#             neibs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
#             for coord in neibs:
#                 x, y = coord
#                 if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
#                     dfs(x, y)
#
#         row, col = len(grid), len(grid[0])
#         r, c = 0, 0
#         count = 0
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == "1":
#                     count += 1
#                     dfs(i, j)
#
#         return count
from Leetcode.t import asrt


class UnionSet:
    def __init__(self, p):
        self.p = p
        self.rank = [0 for _ in p]
        self.count = sum([1 for i in p if i != -1])

    def find(self, i: int) -> int:
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    # 合并两个元素的所在集合
    def union(self, i: int, j: int) -> None:
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                pi, pj = pj, pi
            self.p[pj] = pi
            if self.rank[pi] == self.rank[pj]:
                self.rank[pi] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        total = m * n
        p = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    p.append(i * n + j)
                else:
                    p.append(-1)

        us = UnionSet(p)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1": continue
                cur = i * n + j
                neighbors = [(i, j + 1), (i + 1, j)]
                for x, y in neighbors:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        us.union(cur, x * n + y)

        return us.count


grid = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]]
asrt(Solution, "numIslands", [grid], 1)

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
asrt(Solution, "numIslands", [grid], 1)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

asrt(Solution, "numIslands", [grid], 3)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

asrt(Solution, "numIslands", [grid], 2)
