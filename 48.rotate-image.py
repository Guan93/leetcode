#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    # we can draw a coordinate and find out what flip operations can result in the desired rotation
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


# @lc code=end
