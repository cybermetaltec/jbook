from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 获取周围没打开的格子坐标，和M的数量
        def get_neibs_M_count(x, y):
            # 周围的坐标
            index = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1),
                     (x + 1, y - 1)]
            # 周围没打开格子的坐标
            n_index = [(r, c) for r, c in index if 0 <= r < row and 0 <= c < col and board[r][c] in not_opened_tag]
            # 周围M的数量
            count = sum([board[x][y] == "M" for x, y in n_index])
            return count, n_index

        def open(x, y):
            target = board[x][y]
            if target == "M":
                board[x][y] = "X"
                return

            neib_m, neib_index = get_neibs_M_count(x, y)
            # 周围没有地雷
            if not neib_m:
                board[x][y] = "B"
                for coord in neib_index:
                    open(*coord)
            else:
                board[x][y] = str(neib_m)
                return

        x, y = click
        row, col = len(board), len(board[0])
        not_opened_tag = {"M", "E"}
        if board[x][y] in not_opened_tag:
            open(x, y)

        return board


board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
click = [3, 0]

ret = Solution().updateBoard(board, click)
assert ret == [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"],
               ["B", "B", "B", "B", "B"]]

board = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
click = [1, 2]
ret = Solution().updateBoard(board, click)
assert ret == [["B", "1", "E", "1", "B"], ["B", "1", "X", "1", "B"], ["B", "1", "1", "1", "B"],
               ["B", "B", "B", "B", "B"]],ret
