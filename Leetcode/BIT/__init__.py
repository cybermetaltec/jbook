from typing import Optional, List, Callable


class BIT:
    def __init__(self, arr: List[int], should_update: Callable = lambda x: x):
        self.data = [0] * (len(arr) + 1)
        for i, v in enumerate(arr, 1):
            if uv := should_update(v):
                self.update(i, uv)

    def update(self, i, v):
        while i < len(self.data):
            self.data[i] += v
            i += i & -i

    def get_point(self, p: int):
        p = p + 1
        ret = 0
        while p:
            ret += self.data[p]
            p = p & (p - 1)
        return ret

    def get_block(self, left, right):
        return self.get_point(right) - self.get_point(left - 1)


a = [6, 3, 7, 6, 7, 5, 7, 8, 2, 1]
bit = BIT(a)
print(bit.get_point(4))

b = [3, 0, 4, 5, 4, 8, 3, 2, 2, 5]
bit = BIT(b, lambda x: x > 2)
print(bit.get_block(6, 9))
