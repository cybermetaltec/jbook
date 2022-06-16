from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stuck, mx = [], 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stuck and heights[i] < heights[stuck[-1]]:
                index = stuck.pop()
                mx = max((i - stuck[-1] - 1) * heights[index], mx)
            stuck.append(i)
        print(stuck)
        return mx


nums = [2]
ret = Solution().largestRectangleArea(nums)
print(ret)
