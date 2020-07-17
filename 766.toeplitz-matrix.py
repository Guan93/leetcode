#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#


# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if not self.isDiagonalTheSame(matrix, i, 0):
                return False

        for j in range(n):
            if not self.isDiagonalTheSame(matrix, 0, j):
                return False
        return True

    def isDiagonalTheSame(self, matrix, r, c):
        target = matrix[r][c]
        m, n = len(matrix), len(matrix[0])
        while r < m and c < n:
            if matrix[r][c] != target:
                return False
            r, c = r + 1, c + 1
        return True


# @lc code=end
