class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if count and ord(s[i]) == 32:
                return count
            if ord(s[i]) != 32:
                count += 1
        return count
