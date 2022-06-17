from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stuck, ans = [], 0
        for i in range(len(height)):
            while stuck and height[i] > height[stuck[-1]]:
                lowest = height[stuck.pop()]
                if stuck:
                    left = stuck[-1]
                    width = i - left - 1
                    h = min(height[i], height[left]) - lowest
                    ans += width * h
            stuck.append(i)
        return ans


# nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# nums = [4,2,0,3,2,5]
nums = [1]
print(Solution().trap(nums))
