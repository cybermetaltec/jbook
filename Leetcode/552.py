from Leetcode.t import asrt


# class Solution:
#     def checkRecord(self, n: int) -> int:
#         # dp : [i][A:0,1][L:0,1,2] (n+1)*2*3
#         # 第i天为P:
#         # 今天A为0 昨天A也为0 dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1]+ dp[i-1][0][2]
#         # 今天A为1 昨天A也为1 dp[i][1][0] = dp[i-1][1][0] + dp[i-1][1][1]+ dp[i-1][1][2]
#         # 第i 天为A，i-1天A为0
#         # dp[i][1][0] =  dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
#         # 第i 天为L 1或2 不能为0
#         # dp[i][0][1] = dp[i-1][0][0]
#         # dp[i][0][2] = dp[i-1][0][1]
#         # dp[i][1][1] = dp[i-1][1][0]
#         # dp[i][1][2] = dp[i-1][1][1]
#         # dp = {i: {j: {k: 0 for k in range(3)} for j in range(2)} for i in range(n + 1)}
#         def dp_sum(l):
#             for j in range(2):
#                 for k in range(3):
#                     yield l[n][j][k]
#
#         dp = [[[0, 0, 0], [0, 0, 0]] for i in range(n + 1)]
#         dp[0][0][0], mod = 1, 10 ** 9 + 7
#         for i in range(1, n + 1):
#             for j in range(2):
#                 for k in range(3):
#                     dp[i][j][0] += dp[i - 1][j][k]
#             for k in range(3):
#                 dp[i][1][0] += dp[i - 1][0][k]
#             for k in range(1, 3):
#                 for j in range(2):
#                     dp[i][j][k] += dp[i - 1][j][k - 1]
#         ret = sum(dp_sum(dp)) % mod
#         return ret

class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0], mod = 1, 10 ** 9 + 7
        for i in range(n):
            today = [[0, 0, 0], [0, 0, 0]]
            for j in range(2):
                for k in range(3):
                    today[j][0] += dp[j][k] % mod
            for k in range(3):
                today[1][0] += dp[0][k] % mod
            for k in range(1, 3):
                for j in range(2):
                    today[j][k] += dp[j][k - 1] % mod
            dp = today
        ret = sum((dp[j][k] for j in range(2) for k in range(3))) % mod
        return ret


asrt(Solution, "checkRecord", [2], 8)
asrt(Solution, "checkRecord", [1], 3)
asrt(Solution, "checkRecord", [10101], 183236316)
