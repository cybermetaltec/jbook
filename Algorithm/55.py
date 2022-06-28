from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         i = 0
#         while i < len(nums) - 1:
#             can_jump_to = nums[i + 1:i + nums[i] + 1]
#             if not can_jump_to: return False
#             jump_twice_way = [j + v for j, v in enumerate(can_jump_to)]
#             i += jump_twice_way.index(max(jump_twice_way)) +1
#             if i >= len(nums) - 1: return True
#         return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_index = 0
        for i, v in enumerate(nums):
            if i > furthest_index: return False
            furthest_index = max(furthest_index, i + v)
            if furthest_index >= len(nums) - 1: return True


arr = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
ret = Solution().canJump(arr)
assert ret == True

arr = [3, 2, 1, 0, 4]
ret = Solution().canJump(arr)
assert ret == False
#
arr = [2, 3, 1, 1, 4]
ret = Solution().canJump(arr)
assert ret == True
