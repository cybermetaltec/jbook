from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row=0):
            if row == n:
                return ret.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
            for col in range(n):
                if col not in cols and (row + col) not in left and (row - col) not in right:
                    cols.append(col)
                    left.add(row + col)
                    right.add(row - col)
                    backtrack(row + 1)
                    cols.pop()
                    left.remove(row + col)
                    right.remove(row - col)

        ret, cols, left, right = [], [], set(), set()
        backtrack()
        return ret


print(Solution().solveNQueens(8))
