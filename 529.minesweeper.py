#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            self._updateBoard(board, r, c)
        return board

    def _updateBoard(self, board, r, c):
        count = 0
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0),
                       (1, 1)]:
            new_r, new_c = r + dr, c + dc
            if not (0 <= new_r < len(board)) or not (0 <= new_c < len(board[0])):
                continue
            if board[new_r][new_c] == 'M':
                count += 1

        if count > 0:
            board[r][c] = str(count)
            return

        board[r][c] = 'B'
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0),
                       (1, 1)]:
            new_r, new_c = r + dr, c + dc
            if not (0 <= new_r < len(board)) or not (0 <= new_c < len(board[0])):
                continue
            if board[new_r][new_c] == 'E':
                self._updateBoard(board, new_r, new_c)


# @lc code=end
