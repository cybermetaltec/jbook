class Solution:
    def _lp(self, s: str, l: int, r: int) -> str:
        ret = ""
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                ret = s[l:r + 1]
                l -= 1
                r += 1
            else:
                return ret
        return ret

    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            item_center = self._lp(s, i, i)
            blank_center = self._lp(s, i, i + 1)
            r = item_center if len(item_center) > len(blank_center) else blank_center
            if len(r) > len(ret): ret = r
        return ret


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
