from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def recur(l, r):
            # 如果l=r就是只有一个数返回这个数
            if l == r: return nums[l]
            # l到r的中位序号
            m = (r - l) // 2 + l
            # 左右半边分别求解
            left = recur(l, m)
            right = recur(m + 1, r)

            # 左右解相同
            if left == right: return left
            # 左右解不同 比较两个解在整个数组的的个数
            count_l, count_r = 0, 0
            for i in nums:
                if i == left:
                    count_l += 1
                elif i == right:
                    count_r += 1

            return left if count_l > count_r else right

        return recur(0, len(nums) - 1)


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
