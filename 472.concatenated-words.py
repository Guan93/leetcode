#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#


# @lc code=start
# the problem can break into subproblems of #139. Word Break
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        pre_words = set()
        res = list()
        for word in words:
            if self.wordBreak(word, pre_words):
                res.append(word)
            pre_words.add(word)
        return res

    # O(l^2) where l is the length of word
    def wordBreak(self, word, dictionary):
        if not dictionary:
            return False
        dp = [False] * (len(word) + 1)
        dp[0] = True
        for end in range(1, len(word) + 1):
            for start in range(end):
                if dp[start] and word[start:end] in dictionary:
                    dp[end] = True
                    break
        return dp[-1]


# @lc code=end
