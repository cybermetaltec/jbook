from collections import deque
from typing import List
from unittest import TestCase


# BFS

# class Solution:
#     def slidingPuzzle(self, board: List[List[int]]) -> int:
#         s = "".join([str(c) for r in board for c in r])
#         target = "123450"
#         ex = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
#         pos = s.index("0")
#         q, count, vis = deque([(s, pos)]), 0, {s}
#         while q:
#             for n in range(len(q)):
#                 cur, pos = q.popleft()
#                 if cur == target: return count
#                 new_pos = ex[pos]
#                 for i in new_pos:
#                     copy_s = list(cur)
#                     copy_s[i], copy_s[pos] = copy_s[pos], copy_s[i]
#                     new_s = "".join(copy_s)
#                     if new_s not in vis:
#                         vis.add(new_s)
#                         q.append((new_s, i))
#                         if new_s == target: return count + 1
#             count += 1
#         return -1


class Solution:
    def have_ans(self, s: str) -> bool:
        s, count = [c for c in s if c != "0"], 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if ord(s[i]) > ord(s[j]):
                    count += 1
        return count % 2 == 0

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = "".join([str(c) for r in board for c in r])
        if not self.have_ans(s): return -1
        target = "123450"
        ex = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        pos, vis = s.index("0"), {s: 0}
        q = deque([(s, pos, 0)])
