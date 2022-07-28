class Solution:
    def reverseWords(self, s: str) -> str:
        ret = word = ""
        for char in s:
            if ord(char) != 32:
                word += char
            if word and ord(char) == 32:
                ret = word + " " + ret
                word = ""
        if word: ret = word + " " + ret
        return ret[:-1]


print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("  he  llo wo r  l  d  "))
print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords("a"))
print(Solution().reverseWords("a "))
print(Solution().reverseWords(" a "))
print(Solution().reverseWords(" a  b  c "))
