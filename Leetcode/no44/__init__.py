class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        m, n = len(p) + 1, len(s) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for i in range(1, m):
            if (p_char := p[i - 1]) == "*": dp[i][0] = dp[i - 1][0]
            for j in range(1, n):
                if p_char == "?" or p_char == (s_char := s[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                    if i > 1 and (p_char_prev := p[i - 2]) == "*":
                        dp[i][j] |= dp[i - 2][j - 1]
                elif p_char == "*":
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


assert Solution().isMatch("safgas", "?*g??") is True
assert Solution().isMatch("safgas", "?*") is True
assert Solution().isMatch("safgas", "?****") is True
assert Solution().isMatch("safgas", "?*g?") is False
assert Solution().isMatch("safgas", "?*g*") is True
assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("aa", "aaa") is False
assert Solution().isMatch("aa", "*aa") is True
assert Solution().isMatch("aa", "*aa*") is True
assert Solution().isMatch("aa", "*a*a*") is True
assert Solution().isMatch("aa", "*?*a*") is True
assert Solution().isMatch("aa", "*?*?*") is True
assert Solution().isMatch("aa", "?*?*?*") is False
assert Solution().isMatch("aa", "?*?*") is True
assert Solution().isMatch("aa", "?**?") is True
assert Solution().isMatch("aa", "??**") is True
assert Solution().isMatch("aa", "*") is True
assert Solution().isMatch("cb", "?a") is False
assert Solution().isMatch("adceb", "a*b") is True
assert Solution().isMatch("acdcb", "a*c?b") is False
assert Solution().isMatch("acdcb", "a*cb") is True
assert Solution().isMatch("acdcb", "a*c?") is True
assert Solution().isMatch("", "") is True
assert Solution().isMatch("", "*") is True
assert Solution().isMatch("", "*?") is False
assert Solution().isMatch("", "*****") is True
assert Solution().isMatch("", "?") is False
assert Solution().isMatch("a", "") is False
