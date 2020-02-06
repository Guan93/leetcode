#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for m in range(3):
            for n in range(3):
                matrix = set()
                for i in range(3):
                    for j in range(3):
                        ele = board[m * 3 + i][n * 3 + j]
                        if ele == '.':
                            continue
                        for set_ in [matrix, rows[m * 3 + i], cols[n * 3 + j]]:
                            if ele in set_:
                                return False
                            set_.add(ele)
        return True
# @lc code=end

