#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bt(idx):
            if idx == len(to_fill):
                return True
            r, c = to_fill[idx]
            k = (r // 3) * 3 + (c // 3)  # index of 3x3 squares
            for ele in range(1, 10):
                if ele in rows[r] or ele in cols[c] or ele in sqrs[k]:
                    continue
                board[r][c] = str(ele)
                rows[r].add(ele)
                cols[c].add(ele)
                sqrs[k].add(ele)
                if bt(idx + 1):
                    return True
                else:
                    board[r][c] = '.'
                    rows[r].remove(ele)
                    cols[c].remove(ele)
                    sqrs[k].remove(ele)
            return False

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        to_fill = []

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == '.':
                    to_fill.append((i, j))
                else:
                    ele = int(ele)
                    rows[i].add(ele)
                    cols[j].add(ele)
                    k = (i // 3) * 3 + (j // 3)  # index of 3x3 squares
                    sqrs[k].add(ele)

        bt(0)
        return

# @lc code=end

