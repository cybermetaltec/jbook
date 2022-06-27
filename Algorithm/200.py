from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            grid[r][c] = "0"
            neibs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for coord in neibs:
                x, y = coord
                if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                    dfs(x, y)

        row, col = len(grid), len(grid[0])
        r, c = 0, 0
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
