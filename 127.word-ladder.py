#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#


# @lc code=start
# TLE: O(n^2)
# class Node:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.nei = dict()

#     def is_connected(self, other):
#         return other.val in self.nei

#     def connect(self, other):
#         if not self.is_connected(other):
#             self.nei[other.val] = other
#             other.connect(self)


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         from collections import deque

#         def is_connected(word1, word2):
#             for i in range(len(word1)):
#                 if word1[i] != word2[i]:
#                     return word1[i + 1:] == word2[i + 1:]
#             return False

#         def build_graph(words):
#             graph = dict()
#             for word in words:
#                 if word not in graph:
#                     graph[word] = Node(word)

#             for i in range(len(words)):
#                 for j in range(i + 1, len(words)):
#                     if is_connected(words[i], words[j]):
#                         graph[words[i]].connect(graph[words[j]])
#             return graph

#         if endWord not in wordList:
#             return 0

#         graph = build_graph(wordList + [beginWord])
#         queue = deque([(beginWord, 1)])
#         seen = {beginWord}

#         while queue:
#             word, length = queue.popleft()
#             for nei in graph[word].nei:
#                 if nei not in seen:
#                     if nei == endWord:
#                         return length + 1
#                     queue.append((nei, length + 1))
#                     seen.add(nei)

#         return 0


# # DFS
# class Solution:
#     # O(nL) and O(nL)
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         from collections import defaultdict, deque

#         if endWord not in wordList:
#             return 0

#         L = len(beginWord)
#         all_comb_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 all_comb_dict[f"{word[:i]}*{word[i + 1:]}"].append(word)

#         queue = deque([(beginWord, 1)])
#         seen = {beginWord}

#         while queue:
#             word, length = queue.popleft()

#             for i in range(L):
#                 intermediate = f"{word[:i]}*{word[i + 1:]}"
#                 for nei in all_comb_dict[intermediate]:
#                     if nei not in seen:
#                         if nei == endWord:
#                             return length + 1
#                         seen.add(nei)
#                         queue.append((nei, length + 1))
#                 all_comb_dict[intermediate].clear()
#         return 0

from collections import defaultdict, deque


class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = deque([(beginWord, 1)])  # BFS starting from beginWord
        queue_end = deque([(endWord, 1)])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

# @lc code=end
