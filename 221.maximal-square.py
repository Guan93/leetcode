#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#


# @lc code=start
class Solution:
    # brute force
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     nrows = len(matrix)
    #     ncols = len(matrix[0]) if nrows > 0 else 0

    #     max_sqlen = 0
    #     for i in range(nrows):
    #         for j in range(ncols):
    #             if matrix[i][j] == '1':
    #                 sqlen = 1
    #                 flag = True
    #                 while i + sqlen < nrows and j + sqlen < ncols and flag:
    #                     for k in range(sqlen + 1):
    #                         if matrix[i + sqlen][k + j] == '0':
    #                             flag = False
    #                             break
    #                     for k in range(sqlen + 1):
    #                         if matrix[k + i][j + sqlen] == '0':
    #                             flag = False
    #                             break
    #                     if flag:
    #                         sqlen += 1
    #                 max_sqlen = max(sqlen, max_sqlen)
    #     return max_sqlen * max_sqlen

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0]) if nrows > 0 else 0
        dp = [[0] * (ncols + 1) for _ in range(nrows + 1)]
        max_sqlen = 0
        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    max_sqlen = max(max_sqlen, dp[i][j])
        return max_sqlen * max_sqlen


# @lc code=end
