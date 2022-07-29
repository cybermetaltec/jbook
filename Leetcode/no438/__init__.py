from collections import Counter
from typing import List


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         counter_s = Counter(s[:len(p)])
#         counter_p = Counter(p)
#         ret = []
#         for i in range(0, len(s) - len(p) + 1):
#             remove_char = s[i - 1] if i else None
#             add_char = s[i + len(p) - 1] if i else None
#             if remove_char and add_char and remove_char != add_char:
#                 counter_s[remove_char] -= 1
#                 if counter_s[remove_char] == 0: del counter_s[remove_char]
#                 counter_s[add_char] += 1
#             if counter_p == counter_s: ret.append(i)
#         return ret

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = R = 0
        need, ret, need_count = Counter(p), [], len(p)
        while R < len(s):
            need_count -= need[s[R]] > 0
            need[s[R]] -= 1
            while need_count == 0:
                if need[s[L]] == 0:
                    need_count += 1
                    if R - L + 1 == len(p): ret.append(L)
                need[s[L]] += 1
                L += 1
            R += 1
        return ret

#


print(Solution().findAnagrams("baa", "aa"))
print(Solution().findAnagrams("abab", "ab"))

print(Solution().findAnagrams("abaacbabc", "abc"))
print(Solution().findAnagrams("cbaebabacd", "abc"))
