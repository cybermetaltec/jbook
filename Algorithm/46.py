from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(i=0):
            if len(tmp) == n:
                ret.append(tmp[:])
                return
            for j in range(i,n):
                tmp.append(nums[j])
                nums[i],nums[j] = nums[j],nums[i]
                print(nums)
                backtrace(i+1)
                nums[i],nums[j] = nums[j],nums[i]
                print(nums)
                tmp.pop()

        ret,tmp,n = [],[],len(nums)
        backtrace()
        return ret

print(Solution().permute([1,2,3]))