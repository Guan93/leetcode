#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#


# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = -1
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        count = 0
        res = []
        while count < m * n:
            res.append(matrix[r][c])
            count += 1
            r += direction
            c -= direction
            if not (0 <= r < m) or not (0 <= c < n):
                c += 1
                direction *= -1
                while not (0 <= r < m) or not (0 <= c < n):
                    r += direction
                    c -= direction
        return res



# @lc code=end
