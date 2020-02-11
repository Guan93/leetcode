#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start


class Solution:
    # dfs / bfs: O(n) and O(n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from itertools import product

        def dfs(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'E'

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n:
                    dfs(new_row, new_col)

        def bfs(row, col):
            from collections import deque

            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                if board[row][col] != 'O':
                    continue
                board[row][col] = 'E'

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < m and 0 <= new_col < n:
                        queue.append((new_row, new_col))

        if not board:
            return

        m, n = len(board), len(board[0])
        boarders = (
            list(product([0, m - 1], range(n))) + list(product(range(m), [0, n - 1])))

        for row, col in boarders:
            # dfs(row, col)
            bfs(row, col)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
# @lc code=end
