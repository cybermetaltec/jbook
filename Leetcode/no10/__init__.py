from typing import List


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p) + 1, len(s) + 1
        # dp[i][j]表示 p的前i个字符能否匹配s的前j个字符
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True  # 前0个字符是空字符能匹配空字符
        for i in range(1, m):
            # 这一行主要是字母加*或者.*是能够被忽略的 比如 a*c 能够匹配 c
            if i > 1 and p[i - 1] == "*": dp[i][0] = dp[i - 2][0]
            for j in range(1, n):
                # ij位置的字母相等或者i位置是.
                if p[i - 1] == s[j - 1] or p[i - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]  # 都可以用前i-1个和前j-1个匹配
                    # 字母或.前面是*的情况 可以用*去匹配j-1也可以用*前面的字符还可以不要*和*前面的字符
                    if i > 2 and p[i - 2] == "*": dp[i][j] = dp[i][j] or dp[i - 2][j - 1] or dp[i - 3][j - 1]
                # i指向*
                elif i > 1 and p[i - 1] == "*":
                    # * 前面可以是字母也可以是.
                    if p[i - 2] == s[j - 1] or p[i - 2] == ".":
                        # 等号后面分别是 （* 前面的参与匹配*号本身也参与匹配），（*前面的字符参与匹配，*本身不参与),(*匹配前一个也匹配这一个)
                        dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                    # 不管*号前面是什么，都可以跳过不参与匹配
                    dp[i][j] = dp[i][j] or dp[i - 2][j]

        return dp[-1][-1]


assert Solution().isMatch("bab", "c*a*b") is False
assert Solution().isMatch("aaaab", ".*b") is True
assert Solution().isMatch("aaaab", ".*") is True
assert Solution().isMatch("asdfasdg", ".*") is True
assert Solution().isMatch("aaa", "aaaa") is False
assert Solution().isMatch("aab", "c*a*b") is True
assert Solution().isMatch("aaaab", "aaab.*") is False
assert Solution().isMatch("aaaab", "a*b") is True
assert Solution().isMatch("aaaab", "aaaab.*") is True
assert Solution().isMatch("aaaab", "a*b.*") is True
assert Solution().isMatch("aaaab", "a*b*") is True
assert Solution().isMatch("aaaab", "a*b.") is False
assert Solution().isMatch("ab", ".*") is True
assert Solution().isMatch("aa", "a*") is True
assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("aa", "a.") is True
assert Solution().isMatch("aa", "aa.") is False
assert Solution().isMatch("aa", "aa.*") is True
assert Solution().isMatch("aa", "..") is True
