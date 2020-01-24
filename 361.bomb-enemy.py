class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp1 = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        dp2 = [[(0, 0)] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == '0':
                    dp1[i][j] = (dp1[i][j - 1][0], dp1[i - 1][j][1])
                elif grid[i - 1][j - 1] == 'W':
                    dp1[i][j] = (0, 0)
                elif grid[i - 1][j - 1] == 'E':
                    dp1[i][j] = (dp1[i][j - 1][0] + 1, dp1[i - 1][j][1] + 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if grid[i][j] == '0':
                    dp2[i][j] = (dp2[i][j + 1][0], dp2[i + 1][j][1])
                elif grid[i][j] == 'W':
                    dp2[i][j] = (0, 0)
                elif grid[i][j] == 'E':
                    dp2[i][j] = (dp2[i][j + 1][0] + 1, dp2[i + 1][j][1] + 1)

        max_e = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    max_e = max(max_e, sum(dp1[i + 1][j + 1]) + sum(dp2[i][j]))

        return max_e
