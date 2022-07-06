from Leetcode.t import asrt


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = [1] + [0] * len(s)
#         m = {"1": {str(i) for i in range(10)}, "2": {str(i) for i in range(7)}}
#         for i in range(1, len(dp)):
#             if 0 < int(s[i - 1]) < 10: dp[i] = dp[i - 1]
#             if i >= 2 and s[i - 2] in m and s[i - 1] in m[s[i - 2]]: dp[i] += dp[i - 2]
#         return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        cur, prev, prev2 = 0, 1, 1
        m = {"1": {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, "2": {'0', '1', '2', '3', '4', '5', '6'}}
        for i, v in enumerate(s):
            if 0 < int(v) < 10: cur = prev
            if i >= 1 and s[i - 1] in m and s[i] in m[s[i - 1]]: cur += prev2
            prev2, prev, cur = prev, cur, 0
        return prev


asrt(Solution, "numDecodings", ["2611055971756562"], 4)
asrt(Solution, "numDecodings", ["226"], 3)
asrt(Solution, "numDecodings", ["23124"], 6)
