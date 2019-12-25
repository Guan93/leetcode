#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start

# # brute force O(n^2) and O(1):
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         max_area = 0
#         for i in range(len(heights)):
#             max_width = heights[i]
#             for j in range(i, -1, -1):
#                 max_width = min(max_width, heights[j])
#                 max_area = max(max_area, max_width * (i - j + 1))
#         return max_area


# # divide and conquer: worst O(n^2) if heights is sorted, average O(nlogn); O(1)
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         def _helper(start, end):
#             if start >= len(heights):
#                 return 0
#             if start + 1 >= end:
#                 return heights[start]

#             min_idx = start
#             for i in range(start, end):
#                 if heights[i] < heights[min_idx]:
#                     min_idx = i

#             return max(heights[min_idx] * (end - start), _helper(start, min_idx),
#                        _helper(min_idx + 1, end))

#         return _helper(0, len(heights))


# stack: O(n) and O(n)
class Solution:
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
