import math
from collections import Counter

from Leetcode.t import asrt


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def check_match(m: dict, t: dict) -> bool:
#             if sum(m.values()) >= sum(t.values()):
#                 matched = [v >= t[k] for k, v in m.items()]
#                 return sum(matched) == len(matched)
#             return False
#
#         l = r = 0
#         match_target = {}
#         for i in t:
#             match_target[i] = match_target.get(i, 0) + 1
#         match_str = {i: 0 for i in match_target}
#         ret = (0, math.inf)
#         while l <= r < len(s):
#             while not check_match(match_str, match_target) and r < len(s):
#                 if (key := s[r]) in match_target:
#                     match_str[key] += 1
#                 r += 1
#             while check_match(match_str, match_target):
#                 if ret[1] - ret[0] > r - l:
#                     ret = (l, r)
#                 if s[l] in match_str:
#                     match_str[s[l]] -= 1
#                 l += 1
#         st, e = ret
#         return s[st:e] if e <= len(s) else ""

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         counter = Counter(t)
#         miss = len(t)
#         l = 0
#         for i, v in enumerate(s):
#             miss -= counter[v] > 0
#             counter[v] -= 1
#             while not miss and l <= i:
#                 if s[l] in counter:
#                     counter[v] += 1
#                     miss += 1
#                 l += 1

# class Solution:
#     def minWindow(self, s, t):
#         counter = Counter(t)
#         miss = len(t)
#         # l 是窗口移动指针，L，R是记录结果的
#         l = L = 0
#         R = len(s)
#         # 序号从1开始，方便结果字符切片
#         for i, c in enumerate(s, 1):
#             # t 里的字符才减miss
#             miss -= counter[c] > 0
#             # counter 里的字符代表窗口里还缺少的字符个数，如果是负数，则表示多了
#             counter[c] -= 1
#             # 如果窗口里的字符已经够了，就可以开始删左边的多余字符
#             if not miss:
#                 while counter[s[l]] < 0 and l < i:
#                     counter[s[l]] += 1
#                     l += 1
#                 if i - l < R - L:
#                     R, L = i, l
#         return s[L:R] if not miss else ""

class Solution:
    def minWindow(self, s, t):
        counter = Counter(t)
        miss = len(t)
        # l 是窗口移动指针，L，R是记录结果的
        l = L = R = 0
        # 序号从1开始，方便结果字符切片
        for i, c in enumerate(s, 1):
            # t 里的字符才减miss
            miss -= counter[c] > 0
            # counter 里的字符代表窗口里还缺少的字符个数，如果是负数，则表示多了
            counter[c] -= 1
            # 如果窗口里的字符已经够了，就可以开始删左边的多余字符也就是值为负数的
            # 如果匹配完了最左边是t里的字符，比如"ADOBECODEBANC" "ABC"，L为0指向A,R为5指向C这个时候不会删A，要到A为负数的时候
            # 也就是多了一个A才删，同理如果L指向的是B,那就等到B的记数为负才删
            if not miss:
                while counter[s[l]] < 0 and l < i:
                    counter[s[l]] += 1
                    l += 1
                if not R or i - l < R - L:
                    R, L = i, l
        return s[L:R]


asrt(Solution, "minWindow", ["ADOBECODEBANCFSDF", "ABC"], "BANC")
asrt(Solution, "minWindow", ["a", "a"], "a")
asrt(Solution, "minWindow", ["a", "aa"], "")
