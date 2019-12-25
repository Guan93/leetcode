#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start

# 1. brute force: O((mn)^3) and O(1)

# # 2. dp better brute force on histograms: O(m^2 n) and O(mn)
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         m, n = len(matrix), len(matrix[0])

#         max_area = 0
#         dp = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == '0':
#                     continue
#                 dp[i][j] = dp[i][j - 1] + 1
#                 max_width = dp[i][j]
#                 for k in range(i, -1, -1):
#                     max_width = min(dp[k][j], max_width)
#                     max_area = max(max_width * (i - k + 1), max_area)
#         return max_area


# 3. dp with better algo on histograms: O(mn) and O(mn) (see #84)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        max_area = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i - 1][j] + 1

        for i in range(m):
            max_area = max(max_area, self.largestRectangleArea(dp[i]))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(heights[stack.pop()] * (i - stack[-1] - 1), max_area)
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(heights[stack.pop()] * (len(heights) - stack[-1] - 1),
                           max_area)
        return max_area


# @lc code=end
