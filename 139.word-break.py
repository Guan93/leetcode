#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start
class Solution:
    # bottom-up dp: O(n^2) and O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        can_break = [False] * (n + 1)
        can_break[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if can_break[j] and s[j:i] in wordDict:
                    can_break[i] = True
                    break
        return can_break[n]

    # top-down dp: O(n^2) and O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def _helper(end):
            if end == 0:
                return True
            for start in range(end):
                if _helper(start) and s[start: end] in wordDict:
                    return True
            return False

        wordDict = set(wordDict)
        return _helper(len(s))

# @lc code=end
