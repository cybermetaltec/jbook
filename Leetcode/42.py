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


class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# nums = [4,2,0,3,2,5]
# nums = [1]
print(Solution2().trap(nums))
