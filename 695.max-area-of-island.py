#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0 or seen[r][c]:
                return 0
            seen[r][c] = True
            res = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res += dfs(r + dx, c + dy)
            return res

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]

        res = 0
        for r in range(m):
            for c in range(n):
                if not seen[r][c]:
                    res = max(dfs(r, c), res)
        return res


# @lc code=end
