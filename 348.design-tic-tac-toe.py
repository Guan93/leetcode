# # O(n) per move
# class TicTacToe:

#     def __init__(self, n: int):
#         """
#         Initialize your data structure here.
#         """
#         self.board = [[0] * n for _ in range(n)]
#         self.n = n


#     def move(self, row: int, col: int, player: int) -> int:
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         """
#         self.board[row][col] = player
#         flag = True
#         for i in range(self.n):
#             if self.board[i][col] != player:
#                 flag = False
#                 break
#         if flag:
#             return player

#         flag = True
#         for k in range(self.n):
#             if self.board[row][k] != player:
#                 flag = False
#                 break
#         if flag:
#             return player

#         if row == col:
#             flag = True
#             for k in range(self.n):
#                 if self.board[k][k] != player:
#                     flag = False
#                     break
#             if flag:
#                 return player

#         if row + col == self.n - 1:
#             flag = True
#             for k in range(self.n):
#                 if self.board[k][self.n - 1 - k] != player:
#                     flag = False
#                     break
#             if flag:
#                 return player

#         return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# trade extra space such that move() can be done in O(1)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row_count = {i + 1: [0] * n for i in range(2)}
        self.col_count = {i + 1: [0] * n for i in range(2)}
        self.diag_count = {i + 1: [0, 0] for i in range(2)}

    def move(self, row: int, col: int, player: int) -> int:
        other = player % 2 + 1
        self.row_count[player][row] += 1
        self.row_count[other][row] -= 1
        if self.row_count[player][row] == self.n:
            return player

        self.col_count[player][col] += 1
        self.col_count[other][col] -= 1
        if self.col_count[player][col] == self.n:
            return player

        if row == col:
            self.diag_count[player][0] += 1
            self.diag_count[other][0] -= 1
            if self.diag_count[player][0] == self.n:
                return player

        if row + col == self.n - 1:
            self.diag_count[player][1] += 1
            self.diag_count[other][1] -= 1
            if self.diag_count[player][1] == self.n:
                return player

        return 0
