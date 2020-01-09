#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
import bisect
from collections import defaultdict


class Solution:
    # dp: O(mn) and O(mn)
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     m, n = len(s), len(t)
    #     dp = [[True] * (n + 1)] + [[False] * (n + 1) for _ in range(m)]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == t[j - 1] or dp[i][j - 1]
    #     return dp[-1][-1]

    # binary search: O(len(t) + len(s) * logk) and O(len(t))
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)

        prev = 0
        for c in s:
            j = bisect.bisect_left(idx[c], prev)
            if j == len(idx[c]):
                return False
            prev = idx[c][j] + 1

        return True
# @lc code=end

