#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#


# @lc code=start
class Solution:
    # dp: O(mn) and O(mn)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minpath_sum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    minpath_sum[i][j] = grid[i][j]
                elif i == 0:
                    minpath_sum[i][j] = minpath_sum[i][j - 1] + grid[i][j]
                elif j == 0:
                    minpath_sum[i][j] = minpath_sum[i - 1][j] + grid[i][j]
                else:
                    minpath_sum[i][j] = min(minpath_sum[i - 1][j],
                                            minpath_sum[i][j - 1]) + grid[i][j]
        return minpath_sum[-1][-1]

    # dp: O(mn) and O(n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                path = float("inf")
                if i:
                    path = min(dp[j], path)
                if j:
                    path = min(dp[j - 1], path)
                dp[j] = grid[i][j] + (path if path < float("inf") else 0)

        return dp[-1]

# @lc code=end
