from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(i=0):
            if i == n:
                return ret.append(tmp[:])
            for j in range(n):
                if vis[j]: continue
                vis[j] = 1
                tmp.append(nums[j])
                backtrace(i + 1)
                tmp.pop()
                vis[j] = 0

        nums.sort()
        ret, n, vis, tmp = [], len(nums), [0] * len(nums), []
        backtrace()
        return ret


print(Solution().permuteUnique([1, 1, 2]))
