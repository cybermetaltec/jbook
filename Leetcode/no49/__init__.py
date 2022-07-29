import json
from collections import Counter
from typing import List, ClassVar, Type


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs, m = ["".join(sorted(w)) for w in strs], {}
        for i, v in enumerate(strs):
            arr = m.get(sort_strs[i], [])
            arr.append(v)
            m[sort_strs[i]] = arr
        return list(m.values())


# class Solution:
#     def _hash(self, word: str):
#         l = [0] * 26
#         for s in word:
#             l[97 - ord(s)] += 1
#         return str(l)
#
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashes = [self._hash(s) for s in strs]
#         m = {}
#         for i, v in enumerate(strs):
#             hash = hashes[i]
#             arr = m.get(hash, [])
#             arr.append(v)
#             m[hash] = arr
#
#         return list(m.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
