# class Solution:
#     def mySqrt(self, x: int) -> int:
#         l, r = 0, x
#         ans = 0
#         while int(l) < int(r):
#             mid = (r + l) / 2
#             if mid * mid <= x:
#                 l = mid
#                 ans = mid
#             else:
#                 r = mid
#
#         return int(ans)


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans


ret = Solution().mySqrt(11)
print(ret)
