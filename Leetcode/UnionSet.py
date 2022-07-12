class UnionSet:
    def __init__(self, p, count):
        self.p = p
        self.rank = [0 for _ in p]
        self.count = count

    def find(self, i: int) -> int:
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    # 合并两个元素的所在集合
    def union(self, i: int, j: int) -> None:
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                pi, pj = pj, pi
            self.p[pj] = pi
            if self.rank[pi] == self.rank[pj]:
                self.rank[pi] += 1
            self.count -= 1
