from typing import List


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         step = 0
#         i = 0
#         while i < len(nums) - 1:
#             if i + nums[i] < len(nums) - 1:
#                 can_jump_to = nums[i + 1:i + nums[i] + 1] #当前可以跳的范围
#                 jump2_step = [j + k for j, k in enumerate(can_jump_to)] # 跳两步最远距离
#                 far_index = jump2_step.index(max(jump2_step))
#                 i = i + far_index + 1
#             else:
#                 i = len(nums)
#
#             step += 1
#
#         return step

class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_start_index, jump_end_index = 0, 0
        furthest = 0
        for i, v in enumerate(nums):
            jump_start_index = i + 1
            jump_end_index = i + v



arr = [2, 3, 1, 1, 4]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
# #
arr = [2, 3, 0, 1, 4]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
# #
arr = [2, 3, 1]
ret = Solution().jump(arr)
ans = 1
assert ret == ans, f'{ret}:{ans}'
#
arr = [4, 1, 1, 3, 1, 1, 1]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
#
arr = [1, 1, 1, 1]
ret = Solution().jump(arr)
ans = 3
assert ret == ans, f'{ret}:{ans}'
#
arr = [1, 2, 1, 1, 1]
ret = Solution().jump(arr)
ans = 3
assert ret == ans, f'{ret}:{ans}'

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
ret = Solution().jump(arr)
ans = 2
assert ret == ans, f'{ret}:{ans}'
