#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#


# @lc code=start
# one pass and O(mn) space
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def find_ship(i, j):
            seen.add((i, j))
            if i + 1 < m and board[i + 1][j] == 'X':
                for k in range(i + 1, m):
                    if board[k][j] == '.':
                        break
                    seen.add((k, j))

            elif j + 1 < n and board[i][j + 1] == 'X':
                for k in range(j + 1, n):
                    if board[i][k] == '.':
                        break
                    seen.add((i, k))

        if not board:
            return 0
        m, n = len(board), len(board[0])
        res = 0
        seen = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i, j) not in seen:
                    res += 1
                    find_ship(i, j)

        return res


# one pass and no extra space: we only need to find the "start" of each ship
class Solution2:
    def countBattleships(self, board):
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (
                        j == 0 or board[i][j - 1] == '.'):
                    count += 1
        return count


# @lc code=end
