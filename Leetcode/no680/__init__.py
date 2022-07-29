class Solution:
    def valid(self, s: str, deleted: bool = False) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                if not deleted:
                    return self.valid(s[L + 1:R + 1], True) or self.valid(s[L:R], True)
                else:
                    return False
            L += 1
            R -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.valid(s)


print(Solution().validPalindrome("cbbcc"))
print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("abc"))
