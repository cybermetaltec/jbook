from Leetcode.t import asrt


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = " " + s
        dp = [0] * len(s)
        MAX = 0
        for i in range(1, len(dp)):
            if s[i] == "(": dp[i] = 0
            if s[i] == ")" and i > 1:
                if s[i - 1] == s[i] and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                if s[i - 1] == "(": dp[i] = dp[i - 2] + 2
                MAX = max(MAX, dp[i])
        return MAX


asrt(Solution, "longestValidParentheses", ["(()))())("], 4)
asrt(Solution, "longestValidParentheses", ["()(())"], 6)
asrt(Solution, "longestValidParentheses", ["(()"], 2)
asrt(Solution, "longestValidParentheses", [")(()"], 2)
asrt(Solution, "longestValidParentheses", [")()())"], 4)
asrt(Solution, "longestValidParentheses", [")())())"], 2)
asrt(Solution, "longestValidParentheses", ["(())())"], 6)
asrt(Solution, "longestValidParentheses", ["((())())"], 8)
asrt(Solution, "longestValidParentheses", [""], 0)
