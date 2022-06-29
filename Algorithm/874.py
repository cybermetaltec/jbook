import math
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dir_x = [0, 1, 0, -1]
        dir_y = [1, 0, -1, 0]
        degree = 0
        obstacles = set(map(tuple, obstacles))  # [tuple(o) for o in obstacles]
        max_len = 0

        for i in range(len(commands)):
            command = commands[i]
            if command in (-1, -2):
                degree = (degree + 1) % 4 if command == -1 else (degree - 1) % 4
            if command in range(1, 10):
                x2, y2 = dir_x[degree], dir_y[degree]
                for n in range(command):
                    x1, y1 = x + x2, y + y2
                    if (x1, y1) in obstacles: break
                    x, y = x1, y1
                    max_len = max(max_len, x * x + y * y)

        return max_len


ret = Solution().robotSim([6, -1, -1, 6], [])
assert ret == 36, f'{ret} is not 36'

ret = Solution().robotSim([4, -1, 3], [])
assert ret == 25, f'{ret} is not 25'

ret = Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]])
assert ret == 65, f'{ret} is not 65'
