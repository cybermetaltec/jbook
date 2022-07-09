from collections import Counter
from typing import List

from Leetcode.t import asrt


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m, max_tasks, max_count = Counter(tasks), [], 0
        sorted_m = sorted(m.items(), key=lambda x: x[1], reverse=True)
        max_count = sorted_m[0][1]
        for task in sorted_m:
            if task[1] >= max_count:
                max_tasks.append(task)
                continue
            break
        ret = (max_count - 1) * (n + 1) + len(max_tasks)
        return ret if ret > (mt := len(tasks)) else mt


asrt(Solution, "leastInterval", [["B", "B", "A", "A", "A", "D", "B", "C", "D", "E", "F", "G"], 2], 12)
asrt(Solution, "leastInterval", [["A", "A", "A", "B", "B", "B"], 2], 8)
asrt(Solution, "leastInterval", [["A", "A", "A", "B", "B", "B"], 0], 6)
asrt(Solution, "leastInterval", [["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2], 16)
asrt(Solution, "leastInterval", [["A"], 1], 1)
