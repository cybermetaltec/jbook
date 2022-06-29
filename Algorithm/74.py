from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid // col][mid % col] >= target:
                r = mid
            else:
                l = mid + 1
        return matrix[l // col][l % col] == target


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
Solution().searchMatrix(matrix, target)

# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 3
# assert Solution().searchMatrix(matrix, target) is True
#
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# matrix = [[1], [10], [23]]
# matrix = [[1]]
nums = [j for i in matrix for j in i]
for x in nums:
    assert Solution().searchMatrix(matrix, x) is True
