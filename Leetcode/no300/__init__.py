import bisect
from typing import List


# 动态规划
class Solution0:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        Max = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    Max = max(Max, dp[i])
        return Max


# 二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # last_min_nums[i]代表长度为i+1的子序列最末尾数字的最小值
        last_min_nums = [nums[0]]
        for num in nums[1:]:
            if num > last_min_nums[-1]:
                last_min_nums.append(num)
            else:
                index = bisect.bisect_right(last_min_nums, num)
                if (index and last_min_nums[index - 1] != num) or index == 0: last_min_nums[index] = num

        return len(last_min_nums)
