from typing import List


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         def str_diff_count(s, target):
#             return sum([i != j for i, j in zip(s, target)]) == 1
#
#         def change_find(word: str, new_b_visited: set, target: set[str]) -> bool:
#             # 单词按位换字符 挨个去匹配word_list 排除掉访问过的 也就是这个节点产生的下一层节点
#             new_visited = (
#                 new_word
#                 for i in range(len(word))
#                 for char in char_set
#                 for new_word in [word[:i] + char + word[i + 1:]]
#                 if new_word != word and new_word in word_list
#             )
#             for w in new_visited:
#                 if w in e_visited: return True
#                 if w not in visited:
#                     visited.add(w)
#                     new_b_visited.add(w)
#             return False
#
#         def dfs(paths, path=[], i=0, ret=[]):
#             if i == len(paths):
#                 ret.append(path)
#                 return
#             for j in paths[i]:
#                 if path and str_diff_count(path[-1], j) != 1: continue
#                 dfs(paths, path + [j], i + 1, ret)
#
#             return ret
#
#         word_list = {*wordList}
#         # 特殊情况
#         if not word_list or endWord not in word_list: return []
#         word_list.discard(beginWord)
#         # 所有两个方向访问过的节点，两个方向各自访问过的节点
#         visited, b_visited, e_visited = {beginWord, endWord}, {beginWord}, {endWord}
#         begin_path, end_path = [{beginWord}], [{endWord}]
#         begin_path_c, end_path_c = begin_path, end_path
#         char_set = [chr(i) for i in range(97, 123)]
#         # b_visited 就是当前层的所有节点
#         result = []
#         while b_visited:
#             # 广度遍历是从这一层节点生成下一层的节点，这个交换就是交换当前层，最开始当前层是beginWord
#             # 如果beginWord生成的下一层节点大于1 那下一次当前层就是endWord,这就是所谓的双向
#             if len(b_visited) > len(e_visited):
#                 b_visited, e_visited = e_visited, b_visited
#                 begin_path, end_path = end_path, begin_path
#             # 拿来装产生的下一层节点
#             next_b_visited = set()
#
#             for word in b_visited:
#                 # 每个单词换字符wordList里匹配 如果在wordList里面也不在所有访问过的节点集合visited里面
#                 # 那就是下一层节点，再看它是不是在 e_visited 里面，双向广度遍历的终止条件是 两个方向的访问过的节点有重合
#                 if change_find(word, next_b_visited, e_visited):
#                     paths = begin_path_c + end_path_c[::-1]
#                     result = dfs(paths)
#                     return result
#             # b_visited 改成它产生的下一层所有节点
#             b_visited = next_b_visited
#             begin_path.append(next_b_visited)
#
#         return result

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def str_diff_count(s, target):
            return sum([i != j for i, j in zip(s, target)]) == 1

        def change_find(word: str, new_b_visited: set, target: set[str], b_path) -> bool:
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
        if not word_list or endWord not in word_list: return []
        word_list.discard(beginWord)
        # 所有两个方向访问过的节点，两个方向各自访问过的节点
        visited, b_visited, e_visited = {beginWord, endWord}, {beginWord}, {endWord}
        begin_path, end_path = [], []
        char_set = [chr(i) for i in range(97, 123)]
        # b_visited 就是当前层的所有节点
        result = []
        while b_visited:
            # 广度遍历是从这一层节点生成下一层的节点，这个交换就是交换当前层，最开始当前层是beginWord
            # 如果beginWord生成的下一层节点大于1 那下一次当前层就是endWord,这就是所谓的双向
            if len(b_visited) > len(e_visited):
                b_visited, e_visited = e_visited, b_visited
                begin_path, end_path = end_path, begin_path
            # 拿来装产生的下一层节点
            next_b_visited = set()

            for word in b_visited:
                # 每个单词换字符wordList里匹配 如果在wordList里面也不在所有访问过的节点集合visited里面
                # 那就是下一层节点，再看它是不是在 e_visited 里面，双向广度遍历的终止条件是 两个方向的访问过的节点有重合
                if change_find(word, next_b_visited, e_visited, begin_path):
                    return result
            # b_visited 改成它产生的下一层所有节点
            b_visited = next_b_visited
            begin_path.append(next_b_visited)

        return result


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
ret = Solution().ladderLength(beginWord, endWord, wordList)
ans = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
# print([a == b for a in tuple([tuple(j) for j in ret]) for b in tuple([tuple(i) for i in ans])])
# assert ret == ans, f'ret:{ret}'

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
ret = Solution().ladderLength(beginWord, endWord, wordList)
assert ret == [], f'ret:{ret}'
