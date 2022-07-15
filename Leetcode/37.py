from typing import List

from Leetcode.t import asrt


class Solution:
    def __init__(self):
        self.rows = [0] * 9
        self.cols = [0] * 9
        self.box = [0] * 9
        self.blanks = []
        self.board = []

    # 把某个数记录到行列小方块的二进制中，重复加入同一个数字会还原
    def record(self, i: int, j: int, num: int):
        b = 1 << num
        self.rows[i] ^= b
        self.cols[j] ^= b
        self.box[(i // 3) * 3 + (j // 3)] ^= b

    # 生成某个空格可以填写的数字
    def get_fill_nums(self, i, j) -> List[int]:
        # 记录的时候是第i位为1代表i已经填入，所以二进制一共有10位
        mod = 0b1111111111
        # 把二进制里的0变成1，1是第几位就代表可以填几，直接取反会把高位也变成1，所以要&mod，减1是因为第0位为1,但是格子里不能填0
        # option_b = (~self.rows[i] & mod) & (~self.cols[j] & mod) & (~ self.box[(i // 3) * 3 + (j // 3)] & mod) - 1
        option_b = ~(self.rows[i] | self.cols[j] | self.box[(i // 3) * 3 + (j // 3)]) & mod - 1
        ret = []
        while option_b:
            # 获取最低位的1
            lowest_1 = option_b & -option_b
            # 最低位的1在第几位
            lowest_1_index = bin(lowest_1).count("0") - 1
            ret.append(lowest_1_index)
            # 消除最低位的1，取下一个
            option_b = option_b ^ lowest_1
        return ret

    def fill_blanks(self, i=0):
        # 已经填满
        if i == len(self.blanks): return True
        x, y = self.blanks[i]
        # 获取这个格子可以填的数
        nums = self.get_fill_nums(x, y)
        for num in nums:
            # 加进二进制里面
            self.record(x, y, num)
            self.board[x][y] = str(num)
            # 填入成功 不成功就是nums为空的情况
            if self.fill_blanks(i + 1):
                return True
            else:
                # 二进制要取消之前的操作
                self.record(x, y, num)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        for i in range(9):
            for j in range(9):
                if (num := board[i][j]) == ".":
                    # 把记录三种二进制数据
                    self.blanks.append((i, j))
                else:
                    # 记录待填入数字的坐标
                    self.record(i, j, int(num))
        self.fill_blanks()
        print(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

ret = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
       ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
       ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
       ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
       ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
       ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
       ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
       ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
       ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

assert Solution().solveSudoku(board) == ret
