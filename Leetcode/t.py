import random
from typing import Callable, List, Tuple, Any, ClassVar
from unittest import TestCase


def asrt(cls, func, params, ans, to_tuple=False):
    fn = getattr(cls(), func)
    ret = fn(*params)
    if to_tuple:
        assert tuple(ret) == tuple(ans)
    else:
        assert ret == ans, f'{ret} is not {ans}'


def gen_num_list(n=10, start=0, end=10):
    return [random.randint(start, end) for _ in range(n)]


class TestHelper(TestCase):
    def test_template(self, cases: List[Tuple[List[Any], Any]], SolutionCls: ClassVar, fnName: str,
                      assertFnName: str) -> None:
        for case, ans in cases:
            with self.subTest(case):
                fn = getattr(SolutionCls(), fnName)
                ret = fn(*case)
                assertFn = getattr(self, assertFnName)
                assertFn(ret, ans, f'case:{case},ret:{ret},ans:{ans}')
