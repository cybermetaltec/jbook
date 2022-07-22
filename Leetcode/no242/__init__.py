from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1, m2 = Counter(s), Counter(t)
        return m1 == m2
