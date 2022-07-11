from Leetcode.t import asrt


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s) + 1
#         dp = [[0] * n for _ in range(n)]
#         count = 0
#         for j in range(1, n):
#             for i in range(j - 1, -1, -1):
#                 if j - i == 1 or s[i] == s[j - 1] and (j - i == 2 or (j - i > 2 and dp[i + 1][j - 1])):
#                     count += 1
#                     dp[i][j] = 1
#         return count

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i] = 1
            count += 1
            for j in range(i):
                if s[i] == s[j] and dp[j + 1]:
                    count += 1
                    dp[j] = 1
                else:
                    dp[j] = 0
        return count


asrt(Solution, "countSubstrings", ["abc"], 3)
asrt(Solution, "countSubstrings", ["aaa"], 6)
