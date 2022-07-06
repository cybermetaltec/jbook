from typing import List

from Leetcode.t import asrt


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        dps = [nums[1:], nums[:-1]]
        for dp in dps:
            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(nums) - 1):
                dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])
        return max([dp[-1] for dp in dps])


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1: return nums[0]
#         a = b = c = d = 0
#         for i in range(len(nums) - 1):
#             a, b = b, max(b, a + nums[i])
#             c, d = d, max(d, c + nums[i + 1])
#         return max(b, d)


asrt(Solution, "rob", [[0, 0]], 0)
asrt(Solution, "rob", [[0, 1]], 1)
asrt(Solution, "rob", [[1, 0]], 1)
asrt(Solution, "rob", [[2, 7, 9, 3, 6]], 15)
asrt(Solution, "rob", [[2, 3, 2]], 3)
asrt(Solution, "rob", [[1, 2, 3, 1]], 4)
asrt(Solution, "rob", [[2, 5, 3, 2]], 7)
asrt(Solution, "rob", [[1, 2, 1, 1]], 3)
