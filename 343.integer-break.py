#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            mid = i // 2
            dp.append(max([max(j, dp[j]) * max(i - j, dp[i - j]) for j in range(1, mid + 1)]))
        return dp[-1]

# @lc code=end

