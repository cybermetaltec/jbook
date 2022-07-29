class Solution:
    def isPalindrome(self, s: str) -> bool:
        stuck = [asi for char in s if 97 <= (asi := ord(char.lower())) <= 122 or 48 <= asi <= 57]
        L, R = 0, len(stuck) - 1
        while L < R:
            if stuck[L] != stuck[R]: return False
            L += 1
            R -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("0P"))
