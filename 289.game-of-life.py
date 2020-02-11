#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    # O(N) and O(1)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def update(x, y):
            # 2: 0 -> 1; 3: 1 -> 0
            live_count = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                           (1, -1), (1, 0), (1, 1), (0, 1)]:
                nei_x, nei_y = x + dx, y + dy
                if 0 <= nei_x < m and 0 <= nei_y < n and board[nei_x][nei_y] in [1, 3]:
                    live_count += 1

            if board[x][y] == 1 and (live_count < 2 or live_count > 3):
                board[x][y] = 3
            elif board[x][y] == 0 and live_count == 3:
                board[x][y] = 2

        if not board:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                update(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

# @lc code=end

