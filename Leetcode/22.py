import unittest
from typing import List


class Solution0:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l=0, r=0, path=""):
            if l == n and r == n:
                return ret.append(path)
            if l < n:
                dfs(l + 1, r, path + "(")
            if r < l:
                dfs(l, r + 1, path + ")")

        ret = []
        dfs()
        return ret


# Solution().generateParenthesis(2)
class TestSolution(unittest.TestCase):

    def test_generateParenthesis(self):
        ans_obj = Solution0()
        my = Solution()
        for i in range(1, 9):
            ans = ans_obj.generateParenthesis(i)
            my_ans = my.generateParenthesis(i)
            self.assertEqual(ans, my_ans, f'right:{ans} /n your:{my_ans}')


if __name__ == "__main":
    unittest.main()
