#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            last_row = res[-1]
            res.append([1] + list(map(sum, zip(last_row[1:], last_row[:-1]))) + [1])
        return res

# @lc code=end

