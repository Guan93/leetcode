#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        can_break = [False] * (n + 1)
        can_break[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if can_break[j] and s[j:i] in wordDict:
                    can_break[i] = True
                    break
        return can_break[n]


# @lc code=end
