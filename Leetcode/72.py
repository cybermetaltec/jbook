from Leetcode.t import asrt


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2: return 0
        row, col = len(word1), len(word2)
        if not row or not col: return row or col
        dp = [[i for i in range(col + 1)]] + [[j + 1] + [0] * col for j in range(row)]
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
        return dp[-1][-1]
        #


asrt(Solution, "minDistance", ["ros", "horse"], 3)
asrt(Solution, "minDistance", ["intention", "execution"], 5)
asrt(Solution, "minDistance", ["", "a"], 1)
asrt(Solution, "minDistance", ["", ""], 0)
asrt(Solution, "minDistance", ["a", ""], 1)
asrt(Solution, "minDistance", ["abc", ""], 3)
