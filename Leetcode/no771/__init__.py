class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = len(stones)
        for i in stones:
            if i not in s: count -= 1
        return count
