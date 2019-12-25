#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


# # brute force: O(n^2) and O(1)
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         total_water = 0

#         for i in range(len(height)):
#             high_left = high_right = 0
#             for j in range(i + 1):
#                 high_left = max(high_left, height[j])
#             for j in range(i, len(height)):
#                 high_right = max(high_right, height[j])
#             total_water += min(high_left, high_right) - height[i]
#         return total_water


# # dp: O(n) and O(n)
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         total_water = 0
#         if len(height) <= 1:
#             return 0
#         high_left = [height[0]] * len(height)
#         high_right = [height[-1]] * len(height)
#         for i in range(1, len(height)):
#             high_left[i] = max(high_left[i - 1], height[i])
#         for i in range(len(height) - 2, -1, -1):
#             high_right[i] = max(high_right[i + 1], height[i])
#         for i in range(len(height)):
#             total_water += (min(high_left[i], high_right[i]) - height[i])
#         return total_water


# # stack: O(n) and O(n), each bar can be touched at most twice (insert and pop)
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = current = 0
#         stack = []
#         while current < len(height):
#             while stack and height[current] > height[stack[-1]]:
#                 top = stack.pop()
#                 if not stack:
#                     break
#                 distance = current - stack[-1] - 1
#                 bounded_height = min(height[current], height[stack[-1]]) - height[top]
#                 ans += distance * bounded_height
#             stack.append(current)
#             current += 1
#         return ans


# two pointers: O(n) and O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        total_water = 0
        max_left = height[0]
        max_right = height[-1]
        left, right = 0, len(height) - 1
        while left <= right:
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1
        return total_water


# @lc code=end
