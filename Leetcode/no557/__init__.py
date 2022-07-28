# class Solution:
#     def _reverseWords(self, s: str) -> str:
#         ret = word = ""
#         for char in s:
#             if ord(char) != 32:
#                 word += char
#             if word and ord(char) == 32:
#                 ret = word + " " + ret
#                 word = ""
#         if word: ret = word + " " + ret
#         return ret[:-1]
#
#     def _reverse_str(self, s):
#         arr = list(s)
#         l, r = 0, len(s) - 1
#         while l < r:
#             if arr[l] != arr[r]: arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#             r -= 1
#         return "".join(arr)
#
#     def reverseWords(self, s: str) -> str:
#         s = self._reverse_str(s)
#         s = self._reverseWords(s)
#         return s

# class Solution:
#     def _reverse_str(self, s):
#         arr = list(s)
#         l, r = 0, len(s) - 1
#         while l < r:
#             if arr[l] != arr[r]: arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#             r -= 1
#         return "".join(arr)
#
#     def reverseWords(self, s: str) -> str:
#         ret = word = ""
#         for char in s:
#             if ord(char) != 32:
#                 word += char
#             if word and ord(char) == 32:
#                 ret += self._reverse_str(word) + " "
#                 word = ""
#         if word: ret += self._reverse_str(word) + " "
#         return ret[:-1]
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(["".join(reversed(word)) for word in s.split()])


print(Solution().reverseWords("Let's take LeetCode contest"))
print(Solution().reverseWords("God Ding"))
