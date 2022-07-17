# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             n = n ^ (n & (-n))
#             count += 1
#         return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
