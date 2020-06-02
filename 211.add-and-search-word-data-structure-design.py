#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#


# @lc code=start
class Node:
    def __init__(self) -> None:
        self.val = None
        self.next = dict()


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        i = 0
        node = self.root
        while i < len(word):
            if word[i] not in node.next:
                node.next[word[i]] = Node()
            node = node.next[word[i]]
            i += 1
        node.val = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.root, word)

    def _search(self, node, word):
        if len(word) == 0:
            return node.val is not None

        if word[0] == '.':
            for nxt in node.next:
                if self._search(nxt, word[1:]):
                    return True
        elif word[0] in node.next:
            return self._search(node.next[word[0]], word[1:])

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
