import heapq
import math
from collections import deque
from typing import List


# BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n, count = len(grid), len(grid[0]), 0
        if 1 in (grid[0][0], grid[m - 1][n - 1]): return -1
        q, vis = deque([(0, 0)]), {(0, 0)}
        while q:
            count += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                neighbors = [(i + 1, j),
                             (i - 1, j),
                             (i, j + 1),
                             (i, j - 1),
                             (i + 1, j + 1),
                             (i - 1, j + 1),
                             (i - 1, j - 1),
                             (i + 1, j - 1)]
                for x, y in neighbors:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in vis:
                        q.append((x, y))
                        vis.add((x, y))
                        if x == m - 1 and y == n - 1: return count + 1
        return count if (m - 1, n - 1) in vis else -1


grid = [[0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 11
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 10

grid = [
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 7

grid = [
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == -1

grid = [[0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 25

grid = [[0, 1], [1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 2

grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 4
#
grid = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == -1
#
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 1]
]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == -1

grid = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 3

grid = [
    [0]
]
ret = Solution().shortestPathBinaryMatrix(grid)
assert ret == 1
