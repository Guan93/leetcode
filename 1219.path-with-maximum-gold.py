#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#


# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        def dfs(x, y, s):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return s
            visited[x][y] = True
            ans = max(
                dfs(x - 1, y, s + grid[x][y]), dfs(x + 1, y, s + grid[x][y]),
                dfs(x, y - 1, s + grid[x][y]), dfs(x, y + 1, s + grid[x][y]))
            visited[x][y] = False
            return ans

        ans = 0
        for x in range(m):
            for y in range(n):
                visited = [[False] * n for _ in range(m)]
                ans = max(dfs(x, y, 0), ans)
        return ans


# @lc code=end
