from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        m1, m2 = {}, {}
        for i in range(len(s)):
            if not m1.get(s[i]) and not m2.get(t[i]):
                m1[s[i]] = t[i]
                m2[t[i]] = s[i]
            else:
                if m1.get(s[i]) != t[i] or m2.get(t[i]) != s[i]: return False
        return True


assert Solution().isIsomorphic("badc", "baba") is False
assert Solution().isIsomorphic("bbbaaaba", "aaabbbba") is False
assert Solution().isIsomorphic("egg", "add") is True
assert Solution().isIsomorphic("foo", "bar") is False
assert Solution().isIsomorphic("paper", "title") is True
