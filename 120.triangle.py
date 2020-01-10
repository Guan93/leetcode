#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    # # dp from top to bottom: O(n^2) and O(n^2)
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     dp = [[float("inf")] * (i + 2) for i in range(n + 1)]
    #     dp[0][0] = dp[0][1] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, i + 1):
    #             dp[i][j] = triangle[i - 1][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j])
    #     return min(dp[-1])

    # dp from bottom to top: O(n^2) and O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [_ for _ in triangle[-1]]
        for row in reversed(range(len(triangle) - 1)):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]
# @lc code=end

