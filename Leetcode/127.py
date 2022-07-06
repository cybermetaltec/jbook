from collections import deque
from typing import List


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#
#         def gen_next_level(cur_level_nodes, wordList):
#             ret = []
#             for node in cur_level_nodes:
#                 for i in range(width):
#                     # opts =chars[:ord(node[i])]+chars[ord(node[i])+1:]
#                     for o in chars:
#                         if o == node[i]: continue
#                         str_list = list(node)
#                         str_list[i] = o
#                         new_word = "".join(str_list)
#                         if new_word in wordList:
#                             ret.append(new_word)
#                             wordList.remove(new_word)
#             return ret
#
#         wordList = set(wordList)
#         if not wordList or endWord not in wordList: return 0
#
#         n, width, nodes = len(wordList), len(beginWord), [beginWord]
#         level = 1
#         chars = [chr(i) for i in range(97, 123)]
#         while nodes:
#             for i in nodes:
#                 if i == endWord: return level
#             new_nodes = gen_next_level(nodes, wordList)
#             if nodes:
#                 level += 1
#                 nodes = new_nodes
#             else:
#                 return 0
#         return 0


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def change_word_char(word, index, new_char):
#             str_list = list(word)
#             str_list[index] = new_char
#             return "".join(str_list)
#
#         def change_and_find(word):
#             for i in range(width):
#                 for o in chars:
#                     if o == word[i]: continue
#                     new_word = change_word_char(word, i, o)
#                     if new_word in wordList:
#                         if new_word == endWord: return True
#                         if new_word not in visited:
#                             visited.add(new_word)
#                             q.append(new_word)
#             return False
#
#         wordList, visited = set(wordList), set()
#         if not wordList or endWord not in wordList: return 0
#
#         n, width, q = len(wordList), len(beginWord), deque([beginWord])
#         level = 1
#         chars = [chr(i) for i in range(97, 123)]
#
#         while q:
#             for i in range(len(q)):
#                 word = q.popleft()
#                 if change_and_find(word): return level + 1
#             level += 1
#         return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def change_find(word: str, new_b_visited: set, target: set[str]) -> bool:
            # 单词按位换字符 挨个去匹配word_list 排除掉访问过的 也就是这个节点产生的下一层节点
            new_visited = (
                new_word
                for i in range(len(word))
                for char in char_set
                for new_word in [word[:i] + char + word[i + 1:]]
                if new_word != word and new_word in word_list
            )
            for w in new_visited:
                if w in e_visited: return True
                if w not in visited:
                    visited.add(w)
                    new_b_visited.add(w)
            return False

        word_list = {*wordList}
        # 特殊情况
        if not word_list or endWord not in word_list: return 0
        word_list.discard(beginWord)
        # 所有两个方向访问过的节点，两个方向各自访问过的节点
        visited, b_visited, e_visited = {beginWord, endWord}, {beginWord}, {endWord}
        char_set = [chr(i) for i in range(97, 123)]
        level = 1
        # b_visited 就是当前层的所有节点
        while b_visited:
            # 广度遍历是从这一层节点生成下一层的节点，这个交换就是交换当前层，最开始当前层是beginWord
            # 如果beginWord生成的下一层节点大于1 那下一次当前层就是endWord,这就是所谓的双向
            if len(b_visited) > len(e_visited): b_visited, e_visited = e_visited, b_visited
            # 拿来装产生的下一层节点
            next_b_visited = set()
            for word in b_visited:
                # 每个单词换字符wordList里匹配 如果在wordList里面也不在所有访问过的节点集合visited里面
                # 那就是下一层节点，再看它是不是在 e_visited 里面，双向广度遍历的终止条件是 两个方向的访问过的节点有重合
                if change_find(word, next_b_visited, e_visited):
                    return level + 1
            level += 1
            # b_visited 改成它产生的下一层所有节点
            b_visited = next_b_visited

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
ret = Solution().ladderLength(beginWord, endWord, wordList)
assert ret == 5, ret

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
ret = Solution().ladderLength(beginWord, endWord, wordList)
assert ret == 0, ret

beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
ret = Solution().ladderLength(beginWord, endWord, wordList)
assert ret == 2, ret
