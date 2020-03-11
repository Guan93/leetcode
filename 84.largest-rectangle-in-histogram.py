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
#         def _largest_area(start, end):
#             if start >= end:
#                 return 0
#             min_idx = start
#             for i in range(start, end):
#                 if heights[i] < heights[min_idx]:
#                     min_idx = i

#             return max((end - start) * heights[min_idx],
#                        _largest_area(start, min_idx),
#                        _largest_area(min_idx + 1, end))

#         return _largest_area(0, len(heights))


# monostack: O(n) and O(n)
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


# dp: O(n) and O(n)
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        first_less_left = [-1] * len(heights)
        first_less_right = [len(heights)] * len(heights)

        for i in range(1, len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = first_less_left[p]
            first_less_left[i] = p

        for i in reversed(range(len(heights) - 1)):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = first_less_right[p]
            first_less_right[i] = p

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, (first_less_right[i] - first_less_left[i] - 1) * heights[i])

        return max_area
# @lc code=end
