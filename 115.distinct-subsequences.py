#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#


# @lc code=start
# top-down dp: O(mn) and O(mn)
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]


# optimized space: O(mn) and O(n)
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        old_dp = [0] * (n + 1)
        old_dp[0] = 1

        for i in range(1, m + 1):
            dp = [0] * (n + 1)
            dp[0] = 1
            for j in range(1, n + 1):
                dp[j] = old_dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] += old_dp[j - 1]
            old_dp = dp

        return old_dp[-1]


# @lc code=end
