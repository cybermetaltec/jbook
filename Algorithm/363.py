import math
from typing import List

from Algorithm.t import asrt


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def find(data, k):
            row = data[:]
            for i, v in enumerate(row):
                if i:
                    row[i] = max(row[i] + row[i - 1], row[i])
            row_max = max(row)
            if row_max <= k:
                return row_max
            else:
                closet = -math.inf
                for t in range(len(data)):
                    area = 0
                    for b in range(t, len(data)):
                        area += data[b]
                        if area <= k and abs(area - k) < abs(closet - k): closet = area
                return closet

        m, n = len(matrix), len(matrix[0])
        row_data_map = dict()
        MAX = -math.inf
        for i in range(n):
            row_sum = [0] * m
            for j in range(i, n):
                if j not in row_data_map:
                    row_data_map[j] = [matrix[r][j] for r in range(m)]
                row_data = row_data_map[j]
                row_sum = list(map(sum, zip(row_sum, row_data)))
                MAX = max(MAX, find(row_sum, k))
                if MAX == k: return MAX
        return MAX


matrix = [[1, 0, 1], [0, -2, 3]]
k = 2
asrt(Solution, "maxSumSubmatrix", [matrix, k], 2)
matrix = [[2, 2, -1]]
k = 3
asrt(Solution, "maxSumSubmatrix", [matrix, k], 3)

matrix = [[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
k = -100

asrt(Solution, "maxSumSubmatrix", [matrix, k], -101)
