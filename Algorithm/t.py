import random


def asrt(cls, func, params, ans):
    fn = getattr(cls(), func)
    ret = fn(*params)
    assert ret == ans, f'{ret} is not {ans}'


def gen_num_list(n=10,start=0,end=10):
    return [random.randint(start, end) for _ in range(n)]
