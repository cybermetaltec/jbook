from Algorithm.t import asrt


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1) + 1, len(text2) + 1
        dp = [[0] * n for _ in range(m)]
        for m1 in range(1, m):
            for n1 in range(1, n):
                dp[m1][n1] = (dp[m1 - 1][n1 - 1] + 1) if text1[m1 - 1] == text2[n1 - 1] else max(dp[m1 - 1][n1],
                                                                                                 dp[m1][n1 - 1])
        return dp[-1][-1]


asrt(Solution, "longestCommonSubsequence", ["abcde", "ace"], 3)
asrt(Solution, "longestCommonSubsequence", ["abc", "abc"], 3)
asrt(Solution, "longestCommonSubsequence", ["abc", "def"], 0)
asrt(Solution, "longestCommonSubsequence", ["a", "d"], 0)
asrt(Solution, "longestCommonSubsequence", ["a", "a"], 1)
