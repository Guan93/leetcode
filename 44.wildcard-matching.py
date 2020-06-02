#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lc code=start
# quite similar to #10. regular-expression-matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or i > 0 and dp[i - 1][j]
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], '?')
        return dp[-1][-1]


# @lc code=end
