from typing import List


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         step = 0
#         i = 0
#         while i < len(nums) - 1:
#                 can_jump_to = nums[i + 1:i + nums[i] + 1] #当前可以跳的范围
#                 jump2_step = [j + k for j, k in enumerate(can_jump_to)] # 跳两步最远距离
#                 far_index = jump2_step.index(max(jump2_step))
#                 i = i + far_index + 1
#
#             step += 1
#
#         return step

class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        start, end = 0, 0
        furthest = end
        while end < len(nums) - 1:
            for i in range(start, end + 1):
                furthest = max(furthest, i + nums[i])
            start, end = end + 1, furthest
            step += 1
        return step


#
arr = [2, 3, 1, 1, 4]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
# # # #
arr = [2, 3, 0, 1, 4]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
# # # #
arr = [2, 3, 1]
ret = Solution().jump(arr)
ans = 1
assert ret == ans, f'{ret}:{ans}'
# #
arr = [4, 1, 1, 3, 1, 1, 1]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
# #
arr = [1, 1, 1, 1]
ret = Solution().jump(arr)
ans = 3
assert ret == ans, f'{ret}:{ans}'
# #
arr = [1, 2, 1, 1, 1]
ret = Solution().jump(arr)
ans = 3
assert ret == ans, f'{ret}:{ans}'
#
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
