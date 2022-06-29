class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= num:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans * ans == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        while num > 0:
            num -= odd
            odd += 2
        return num == 0


print(Solution().isPerfectSquare(9))
