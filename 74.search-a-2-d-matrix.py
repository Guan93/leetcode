#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

# two binary search: O(log(m)) + O(log(n)) = O(log(mn))
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
#         anchors = [row[0] for row in matrix]
#         target_row = self._binary_search(anchors, target, 0, len(anchors) - 1)
#         if target_row < 0:
#             return False
#         target_col = self._binary_search(matrix[target_row], target, 0, len(matrix[0]) - 1)
#         if target_col < 0:
#             return False
#         return matrix[target_row][target_col] == target

#     def _binary_search(self, a: List, target: int, low: int, high: int) -> int:
#         if low == high:
#             return low - 1 if target < a[low] else low
#         mid = low + (high - low) // 2
#         if a[mid] == target:
#             return mid
#         elif target < a[mid]:
#             return self._binary_search(a, target, low, mid)
#         else:
#             return self._binary_search(a, target, mid + 1, high)

# one binary search: O(log(mn))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]
            if target == mid_val:
                return True
            elif target < mid_val:
                right = mid - 1
            else:
                left = mid + 1

        return False

# @lc code=end
