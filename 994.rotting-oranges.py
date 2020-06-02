#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        level = 0
        while queue:
            row, col, level = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, level + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return level

# @lc code=end

