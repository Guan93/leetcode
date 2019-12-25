#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curr = 0
        if len(board) < 1 or len(board[0]) < 1:
            return False
        marked = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, curr, i, j, marked):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, curr: int, row: int, col: int,
            marked: List[List[bool]]) -> bool:
        if curr == len(word):
            return True
        if (row < 0 or row == len(board) or col < 0 or col == len(board[0])
                or board[row][col] != word[curr] or marked[row][col]):
            return False

        marked[row][col] = True
        if (self.dfs(board, word, curr + 1, row, col - 1, marked)
                or self.dfs(board, word, curr + 1, row, col + 1, marked)
                or self.dfs(board, word, curr + 1, row - 1, col, marked)
                or self.dfs(board, word, curr + 1, row + 1, col, marked)):
            return True
        marked[row][col] = False
        return False


# @lc code=end
