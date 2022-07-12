from typing import List

from Leetcode.t import asrt


class Solution0:
    # 查询某个元素的所属集合
    def unionFind(self, p: List[int], i: int) -> int:
        parent_index = i
        while p[parent_index] != parent_index:
            parent_index = p[parent_index]

        return parent_index

    # 合并两个元素的所在集合
    def union(self, p: List[int], i: int, j: int) -> int:
        pi = self.unionFind(p, i)
        pj = self.unionFind(p, j)
        if pi != pj:
            if pj != j:
                for k in range(len(p)):
                    if p[k] == pj:
                        p[k] = pi
            else:
                p[pj] = pi

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        p = [x for x in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1 and p[i] != p[j]:
                    self.union(p, i, j)
        return len(set(p))


class Solution:
    # 查询某个元素的所属集合
    def unionFind(self, p: List[int], i: int) -> int:
        parent_index = i
        while p[parent_index] != parent_index:
            parent_index = p[parent_index]

        # 路径压缩
        while p[i] != i:
            cur = i  # 当前元素的序号
            i = p[i]  # 检查父节点是不是根节点
            p[cur] = parent_index

        return parent_index

    # 合并两个元素的所在集合
    def union(self, p: List[int], i: int, j: int) -> int:
        pi = self.unionFind(p, i)
        pj = self.unionFind(p, j)
        p[pj] = pi

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        p = [x for x in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union(p, i, j)
        ret = {self.unionFind(p, i) for i in range(n)}
        return len(ret)


# asrt(Solution, "findCircleNum", [[
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]
# ]], 2)
asrt(Solution, "findCircleNum", [
    [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]
], 1)
asrt(Solution, "findCircleNum", [
    [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]
], 6)
asrt(Solution, "findCircleNum", [[
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
]], 1)
asrt(Solution, "findCircleNum", [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]], 3)
