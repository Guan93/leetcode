#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#


# @lc code=start
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j, memo):
            if memo[i][j] > 0:
                return memo[i][j]
            for r, c in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if (0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[i][j]):
                    memo[i][j] = max(memo[i][j], dfs(r, c, memo))
            memo[i][j] += 1
            return memo[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, memo))
        return ans


# @lc code=end
