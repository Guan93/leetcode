#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return [""]
            res = []
            for word in wordDict:
                if len(word) <= len(s) - i and s[i:i + len(word)] == word:
                    for sentence in dfs(i + len(word)):
                        res.append(word + " " + sentence)
            memo[i] = res
            return res
        memo = dict()
        return [sentence.strip() for sentence in dfs(0)]

# @lc code=end

