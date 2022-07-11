from typing import List

from Leetcode.t import asrt


# class Trie:
#
#     def __init__(self):
#         self.data = {}
#
#     def insert(self, word: str) -> None:
#         root = self.data
#         for i, v in enumerate(word, 1):
#             if m := root.get(v):
#                 root = m
#             else:
#                 root[v] = {}
#                 root = root[v]
#         root["word"] = word
#
#     def _search(self, word: str, all=True) -> bool:
#         root = self.data
#         for v in word:
#             if m := root.get(v):
#                 root = m
#             else:
#                 return False
#         if not all: return True if root else False
#         return True if root.get("word") == word else False
#
#     def search(self, word: str) -> bool:
#         return self._search(word)
#
#     def startsWith(self, prefix: str) -> bool:
#         return self._search(prefix, False)
#
#
# class Solution:
#     def __init__(self):
#         self.trie = Trie()
#         self.vis = set()
#         self.ret = []
#
#     def dfs(self, i, j, board, trie):
#         m, n = len(board), len(board[0])
#         s = board[i][j]
#         if s not in trie: return
#         child = trie.get(s)
#         if not child:
#             del trie[s]
#             return
#         if word := child.get("word"):
#             self.ret.append(word)
#             del child["word"]
#
#         board[i][j] = "#"
#         for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
#             if 0 <= r < m and 0 <= c < n:
#                 self.dfs(r, c, board, child)
#         board[i][j] = s
#
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m, n = len(board), len(board[0])
#         i = j = 0
#         for word in set(words):
#             self.trie.insert(word)
#         for i in range(m):
#             for j in range(n):
#                 self.dfs(i, j, board, self.trie.data)
#         return self.ret

# class Trie:
#
#     def __init__(self):
#         self.data = {}
#
#     def insert(self, word: str) -> None:
#         root = self.data
#         for i, v in enumerate(word, 1):
#             if m := root.get(v):
#                 root = m
#             else:
#                 root[v] = {}
#                 root = root[v]
#         root["$"] = True
#
#     def _search(self, word: str, all=True) -> bool:
#         root = self.data
#         for v in word:
#             if m := root.get(v):
#                 root = m
#             else:
#                 if v in root: del root[v]
#                 return False
#         if not all: return True if root else False
#         return True if root.get("$") else False
#
#     def search(self, word: str) -> bool:
#         return self._search(word)
#
#     def startsWith(self, prefix: str) -> bool:
#         return self._search(prefix, False)
#
#     def delete(self, word):
#         prev = cur = self.data
#         for v in word:
#             if ne := cur.get(v):
#                 cur, prev = ne, cur
#             else:
#                 del cur[v]
#                 return
#         del cur["$"]
#         if not cur: del prev[word[-1]]
#         return True
#
#
# class Solution:
#     def __init__(self):
#         self.trie = Trie()
#         self.vis = set()
#         self.ret = []
#
#     def dfs(self, i, j, board, path):
#         m, n = len(board), len(board[0])
#         s = board[i][j]
#         path += s
#         if not self.trie.startsWith(path): return
#         if self.trie.search(path):
#             self.ret.append(path)
#             self.trie.delete(path)
#
#         board[i][j] = "#"
#         for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
#             if 0 <= r < m and 0 <= c < n:
#                 self.dfs(r, c, board, path)
#         board[i][j] = s
#
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m, n = len(board), len(board[0])
#         i = j = 0
#         for word in set(words):
#             self.trie.insert(word)
#         for i in range(m):
#             for j in range(n):
#                 self.dfs(i, j, board, "")
#         return self.ret


# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
# # words = ["oath", "pea", "eat", "rain"]
# words = ["oa", "oaa"]
#
# ret = Solution().findWords(board, words)
# print(ret)
#
# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
# words = ["oath", "pea", "eat", "rain"]
#
# ret = Solution().findWords(board, words)
# print(ret)

class Trie:

    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        root = self.data
        for i, v in enumerate(word, 1):
            if m := root.get(v):
                root = m
            else:
                root[v] = {}
                root = root[v]
        root["word"] = word


class Solution:
    def __init__(self):
        self.trie = Trie()
        self.vis = set()
        self.ret = []

    def dfs(self, i, j, board, trie):
        m, n = len(board), len(board[0])
        s = board[i][j]
        if s not in trie: return
        child = trie.get(s)
        if not child:
            del trie[s]
            return
        if word := child.get("word"):
            self.ret.append(word)
            del child["word"]

        board[i][j] = "#"
        for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= r < m and 0 <= c < n:
                self.dfs(r, c, board, child)
        board[i][j] = s

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        i = j = 0
        for word in set(words):
            self.trie.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, board, self.trie.data)
        return self.ret


board = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
words = ["lllllll", "fffffff", "ssss", "s", "rr", "xxxx", "ttt", "eee", "ppppppp", "iiiiiiiii", "xxxxxxxxxx", "pppppp",
         "xxxxxx", "yy", "jj", "ccc", "zzz", "ffffffff", "r", "mmmmmmmmm", "tttttttt", "mm", "ttttt", "qqqqqqqqqq", "z",
         "aaaaaaaa", "nnnnnnnnn", "v", "g", "ddddddd", "eeeeeeeee", "aaaaaaa", "ee", "n", "kkkkkkkkk", "ff", "qq",
         "vvvvv", "kkkk", "e", "nnn", "ooo", "kkkkk", "o", "ooooooo", "jjj", "lll", "ssssssss", "mmmm", "qqqqq",
         "gggggg", "rrrrrrrrrr", "iiii", "bbbbbbbbb", "aaaaaa", "hhhh", "qqq", "zzzzzzzzz", "xxxxxxxxx", "ww",
         "iiiiiii", "pp", "vvvvvvvvvv", "eeeee", "nnnnnnn", "nnnnnn", "nn", "nnnnnnnn", "wwwwwwww", "vvvvvvvv",
         "fffffffff", "aaa", "p", "ddd", "ppppppppp", "fffff", "aaaaaaaaa", "oooooooo", "jjjj", "xxx", "zz", "hhhhh",
         "uuuuu", "f", "ddddddddd", "zzzzzz", "cccccc", "kkkkkk", "bbbbbbbb", "hhhhhhhhhh", "uuuuuuu", "cccccccccc",
         "jjjjj", "gg", "ppp", "ccccccccc", "rrrrrr", "c", "cccccccc", "yyyyy", "uuuu", "jjjjjjjj", "bb", "hhh", "l",
         "u", "yyyyyy", "vvv", "mmm", "ffffff", "eeeeeee", "qqqqqqq", "zzzzzzzzzz", "ggg", "zzzzzzz", "dddddddddd",
         "jjjjjjj", "bbbbb", "ttttttt", "dddddddd", "wwwwwww", "vvvvvv", "iii", "ttttttttt", "ggggggg", "xx", "oooooo",
         "cc", "rrrr", "qqqq", "sssssss", "oooo", "lllllllll", "ii", "tttttttttt", "uuuuuu", "kkkkkkkk", "wwwwwwwwww",
         "pppppppppp", "uuuuuuuu", "yyyyyyy", "cccc", "ggggg", "ddddd", "llllllllll", "tttt", "pppppppp", "rrrrrrr",
         "nnnn", "x", "yyy", "iiiiiiiiii", "iiiiii", "llll", "nnnnnnnnnn", "aaaaaaaaaa", "eeeeeeeeee", "m", "uuu",
         "rrrrrrrr", "h", "b", "vvvvvvv", "ll", "vv", "mmmmmmm", "zzzzz", "uu", "ccccccc", "xxxxxxx", "ss", "eeeeeeee",
         "llllllll", "eeee", "y", "ppppp", "qqqqqq", "mmmmmm", "gggg", "yyyyyyyyy", "jjjjjj", "rrrrr", "a", "bbbb",
         "ssssss", "sss", "ooooo", "ffffffffff", "kkk", "xxxxxxxx", "wwwwwwwww", "w", "iiiiiiii", "ffff", "dddddd",
         "bbbbbb", "uuuuuuuuu", "kkkkkkk", "gggggggggg", "qqqqqqqq", "vvvvvvvvv", "bbbbbbbbbb", "nnnnn", "tt", "wwww",
         "iiiii", "hhhhhhh", "zzzzzzzz", "ssssssssss", "j", "fff", "bbbbbbb", "aaaa", "mmmmmmmmmm", "jjjjjjjjjj",
         "sssss", "yyyyyyyy", "hh", "q", "rrrrrrrrr", "mmmmmmmm", "wwwww", "www", "rrr", "lllll", "uuuuuuuuuu", "oo",
         "jjjjjjjjj", "dddd", "pppp", "hhhhhhhhh", "kk", "gggggggg", "xxxxx", "vvvv", "d", "qqqqqqqqq", "dd",
         "ggggggggg", "t", "yyyy", "bbb", "yyyyyyyyyy", "tttttt", "ccccc", "aa", "eeeeee", "llllll", "kkkkkkkkkk",
         "sssssssss", "i", "hhhhhh", "oooooooooo", "wwwwww", "ooooooooo", "zzzz", "k", "hhhhhhhh", "aaaaa", "mmmmm"]

ret = Solution().findWords(board, words)
print(ret)
