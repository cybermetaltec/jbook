from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         for i in range(len(strs[0])):
#             for j in range(1, len(strs)):
#                 if i >= len(strs[j]) or strs[0][i] != strs[j][i]: return strs[0][:i]
#         return strs[0]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0] if strs else ""
        if len(strs) == 2:
            left, right, i = strs[0], strs[1], 0
            for i, v in enumerate(left):
                if i >= len(right) or v != right[i]: return left[:i]
            return left
        mid = len(strs) >> 1
        l = self.longestCommonPrefix(strs[:mid])
        r = self.longestCommonPrefix(strs[mid:])
        ret = self.longestCommonPrefix([l, r])
        return ret
