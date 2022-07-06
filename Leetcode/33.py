from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            if nums[r] < nums[mid] < target or nums[mid] < target <= nums[r] or (
                    target < nums[l] and nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid - 1

        return l if nums[l] == target else -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
ret = Solution().search(nums, target)
assert ret == 4, ret
#
ret = Solution().search(nums, 3)
assert ret == -1, ret

ret = Solution().search([1, 3], 3)
assert ret == 1, ret

ret = Solution().search([1, 3], 1)
assert ret == 0, ret

ret = Solution().search([5, 3], 5)
assert ret == 0, ret

ret = Solution().search([5, 3], 3)
assert ret == 1, ret

ret = Solution().search([1, 2, 3], 1)
assert ret == 0, ret

ret = Solution().search([1, 2, 3], 2)
assert ret == 1, ret

ret = Solution().search([1, 2, 3], 3)
assert ret == 2, ret

ret = Solution().search([3, 1, 2], 3)
assert ret == 0, ret

ret = Solution().search([3, 1, 2], 1)
assert ret == 1, ret

ret = Solution().search([3, 1, 2], 2)
assert ret == 2, ret

ret = Solution().search([2, 3, 1], 2)
assert ret == 0, ret

ret = Solution().search([2, 3, 1], 3)
assert ret == 1, ret

ret = Solution().search([2, 3, 1], 1)
assert ret == 2, ret
