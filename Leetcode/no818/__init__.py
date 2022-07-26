class Solution:
    def __init__(self):
        self.vis = {0: 0, 1: 1}

    def racecar(self, target: int) -> int:
        if (mem := self.vis.get(target)) is not None: return mem
        ret = 0
        # 位运算 2的N次方的二进制只有一个1
        # 连续n个A走的距离是2**A-1
        if (target + 1) & target == 0:
            # 取得是2的几次方，也就是走了多少步刚好到这个位置
            ret = bin(target + 1).count("0") - 1
        else:
            # 不能一次到位，那这个数的二进制就不是连续n个1的形式
            # bin返回的字符串是0b开头，后面有几个字符最多就是几个1
            # 比如9的二进制是0b1001，那超过9的2的N次方就是0b1111，小于9的2的N次方就是0b111
            blow = len(bin(target)) - 3
            over = blow + 1
            # 如果超过目标位置，就相当于调一次头然后再次从起点走到超过的距离位置
            # 步数 = 到达超过目标位置的步数+转向+从0到超过的长度位置的步数
            over_to_target = (1 << over) - 1 - target
            ret = over + self.racecar(over_to_target) + 1
            # 目标点前面的2**n-1位置
            blow_pos = (1 << blow) - 1
            # 这个时候可以就是往后退 退0步到blow-1步，退0步的意思就是掉个头再掉个头
            # 相当于位置不变把速度重置为1，挨个试，取最小的
            # 不管退几步都要掉两次头
            for back_step in range(0, blow):
                back_point = blow_pos - (1 << back_step) + 1
                back_point_to_target = self.racecar(target - back_point) + 1
                ret = min(ret, blow + back_step + 1 + back_point_to_target)
        # 缓存结果
        self.vis[target] = ret
        return ret
