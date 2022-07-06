from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            # if nums[l] <= nums[mid] <= nums[r]:
            #     return nums[l]
            # if nums[l] >= nums[mid] >= nums[r]:
            #     return nums[r]
            # if nums[l] < nums[mid] > nums[r]:
            #     l = mid
            # if nums[l] > nums[mid] < nums[r]:
            #     r = mid
        return nums[l]


assert Solution().findMin([3, 4, 5, 1, 2]) == 1
assert Solution().findMin([2, 3, 4, 5, 1]) == 1
assert Solution().findMin([1, 2, 3, 4, 5]) == 1
assert Solution().findMin([5, 1, 2, 3, 4]) == 1
assert Solution().findMin([4, 5, 1, 2, 3]) == 1
assert Solution().findMin([3, 4, 5, 1, 2]) == 1
assert Solution().findMin([2, 3, 4, 5, 1]) == 1
assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert Solution().findMin([11, 13, 15, 17]) == 11
assert Solution().findMin([17, 11, 13, 15]) == 11
assert Solution().findMin([15, 17, 11, 13]) == 11
assert Solution().findMin([1]) == 1
assert Solution().findMin([2, 1]) == 1
assert Solution().findMin([1, 2]) == 1
assert Solution().findMin([1, 2, 3]) == 1
assert Solution().findMin([3, 1, 2]) == 1
assert Solution().findMin([2, 3, 1]) == 1
