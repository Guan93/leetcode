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
#         dp = [[0] * n for _ in range(m)]
#         max_rec = 0

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == '1':
#                     dp[i][j] = 1 + (dp[i][j - 1] if j > 0 else 0)
#                     k = i
#                     curr_width = float("inf")
#                     while k >= 0 and dp[k][j] > 0:
#                         curr_width = min(dp[k][j], curr_width)
#                         max_rec = max(curr_width * (i - k + 1), max_rec)
#                         k -= 1
#         return max_rec


# 3. dp with better algo on histograms: O(mn) and O(n) (see #84)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        max_area = 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(dp))

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


# 4. dp: O(mn) and O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n
        max_area = 0

        for i in range(m):
            curr_left, curr_right = 0, n
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    left[j], curr_left = 0, j + 1
            #update right
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = n, j
            # update height and max_area
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


# @lc code=end
