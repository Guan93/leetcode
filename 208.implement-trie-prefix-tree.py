#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from typing import List, Optional

R = 26


class TreeNode:
    def __init__(self) -> None:
        self.next: "List[Optional[TreeNode]]" = [None for _ in range(R)]
        self.is_end = False


# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self._root = TreeNode()
#         self._size = 0

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         if not self.search(word):
#             self._insert(self._root, word, 0)

#     def _insert(self, x: Optional[TreeNode], word: str, d: int) -> TreeNode:
#         if x is None:
#             x = TreeNode()
#         if d == len(word):
#             self._size += 1
#             x.is_end = True
#             return x
#         i = ord(word[d]) - ord('a')
#         x.next[i] = self._insert(x.next[i], word, d + 1)
#         return x

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         return self._search(self._root, word, 0)

#     def _search(self, x: Optional[TreeNode], word: str, d: int) -> bool:
#         if x is None:
#             return False
#         if d == len(word):
#             return x.is_end
#         i = ord(word[d]) - ord('a')
#         return self._search(x.next[i], word, d + 1)

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         return self._startsWith(self._root, prefix, 0)

#     def _startsWith(self, x: Optional[TreeNode], prefix: str, d: int) -> bool:
#         if x is None:
#             return False
#         if d == len(prefix):
#             return True
#         i = ord(prefix[d]) - ord('a')
#         return self._startsWith(x.next[i], prefix, d + 1)


class Trie:
    def __init__(self) -> None:
        self._root = TreeNode()

    def search(self, word: str) -> bool:
        curr = self._root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.next[i]:
                return False
            curr = curr.next[i]
        return curr.is_end

    def insert(self, word: str) -> None:
        curr = self._root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.next[i]:
                curr.next[i] = TreeNode()
            curr = curr.next[i]
        curr.is_end = True

    def startsWith(self, prefix: str) -> bool:
        curr = self._root
        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.next[i]:
                return False
            curr = curr.next[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
