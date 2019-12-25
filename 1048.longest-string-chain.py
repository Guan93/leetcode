#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start


# # dp: O(nlogn + ns^2) (construct a string also takes time) and O(ns)
# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         dp = dict()
#         for word in sorted(words, key=len):
#             max_for_word = 0
#             for i in range(len(word)):
#                 max_for_word = max(dp.get(word[:i] + word[i + 1:], 0) + 1, max_for_word)
#             dp[word] = max_for_word
#         return max(dp.values())

# dfs: O(n + ns^2) and O(ns)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        memo = dict()

        def dfs(word, memo, word_set):
            if word not in word_set:
                return 0
            max_for_word = 0
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1:]
                if prev_word in memo:
                    max_for_word = max(memo[prev_word] + 1, max_for_word)
                else:
                    max_for_word = max(dfs(prev_word, memo, word_set) + 1, max_for_word)
            memo[word] = max_for_word
            return memo[word]
        for word in words:
            dfs(word, memo, word_set)
        return max(memo.values())


# @lc code=end
