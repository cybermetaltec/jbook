class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        while n:
            lowest_1 = n & (-n)
            lowest_1_index = bin(lowest_1).count("0") - 1
            ans += 1 << (31 - lowest_1_index)
            n = n ^ lowest_1
        return ans
