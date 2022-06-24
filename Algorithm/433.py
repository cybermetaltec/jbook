from collections import deque
from typing import List


# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:

# def strChangeOnce(s, target):
#     count = 0
#     for i in range(len(s)):
#         if s[i] != target[i]:
#             count += 1
#             if count > 1: return
#     if count == 1:
#         return target
#
# def strChangeToBankInOnce(s, bank: set[str]) -> List[str]:
#     ret = []
#     for j in bank:
#         if strChangeOnce(s, j):
#             ret.append(j)
#     for r in ret:
#         bank.remove(r)
#     return ret
#
# count, bank, start = 0, set(bank), deque([start])
# ret = []
# while start:
#     print(start)
#     s = start.popleft()
#     print(s)
#     print("------------")
#     if s == end:
#         ret.append(count + 1)
#     if strChangeOnce(s, end):
#         ret.append(count + 1)
#     else:
#         new_changes = strChangeToBankInOnce(s, bank)
#         if new_changes:
#             count += 1
#             start += new_changes
# print(ret)
# return sum(ret) if ret else -1

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 判断两个字符串是否只有一个字符不一样
        def str_diff_count(s, target):
            return sum([i != j for i, j in zip(s, target)]) == 1

        # 筛选出列表中与传入的字符串只有一个字符不一样的字符串
        def str_transformed(s, target: set[str]) -> List[str]:
            return [j for j in target if str_diff_count(s, j)]

        def bfs(nodes: List[str], target: set[str], level=0):
            children = []
            for node in nodes:
                if node == end and end in bank:
                    return level
                children += str_transformed(node, target)
            new_target = target - set(children)
            return bfs(children, new_target, level + 1) if children else -1

        t = set(bank)
        # start in t and t.remove(start)
        ret = bfs([start], t) if bank else -1
        return ret


start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
assert Solution().minMutation(start, end, bank) == 1

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
assert Solution().minMutation(start, end, bank) == 2

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
assert Solution().minMutation(start, end, bank) == 3

#
start = "AACCGGTT"
end = "AACCGGTA"
bank = []
assert Solution().minMutation(start, end, bank) == -1

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]
assert Solution().minMutation(start, end, bank) == 4

start = "AAAACCCC"
end = "CCCCCCCC"
bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]

assert Solution().minMutation(start, end, bank) == 4

start = "AACCTTGG"
end = "AATTCCGG"
bank = ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]
assert Solution().minMutation(start, end, bank) == -1
