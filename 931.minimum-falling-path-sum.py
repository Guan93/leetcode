#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n = len(A), len(A[0])
        dp = [[float("inf")] * (n + 2) for _ in range(m)]
        for j in range(n):
            dp[0][j + 1] = A[0][j]

        for i in range(1, m):
            for j in range(1, n + 1):
                dp[i][j] = A[i][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[-1])
# @lc code=end

