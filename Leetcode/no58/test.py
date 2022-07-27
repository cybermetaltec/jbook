import random
import unittest

from Leetcode.t import TestHelper
from Leetcode.no58 import Solution

blanks = [" " * random.randint(0, 5) for _ in range(100)]
gen_char = lambda: chr(random.choice([i for i in range(65, 91)] + [j for j in range(97, 123)]))
gen_word = lambda: "".join([gen_char() for _ in range(random.randint(5, 100))])
words = [gen_word() for _ in range(1000)]


def gen_sentence():
    sen = [random.choice(words) for _ in range(10, 30)]

    for _ in range(random.randint(3, 10)):
        sen[random.randint(0, len(sen) - 1)] = random.choice(blanks)
    return " ".join(sen)


class MyTestCase(TestHelper):
    def test_something(self):
        sens = [gen_sentence() for _ in range(100)]
        cases1 = [([s], len(s.split()[-1])) for s in sens]
        cases2 = [(["Hello World"], 5),
                  (["   fly me   to   the moon  "], 4),
                  (["luffy is still joyboy"], 6),
                  (["a"], 1),
                  ]
        self.test_template(cases1, Solution, "lengthOfLastWord", "assertEqual")
        self.test_template(cases2, Solution, "lengthOfLastWord", "assertEqual")


if __name__ == '__main__':
    unittest.main()
