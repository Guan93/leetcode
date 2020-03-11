#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
# # binary search: O(nlog(n)) and O(1)
# # can simply do binary serach on each row and get same complexity
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         def binary_search(a, target, lo, hi):
#             while lo < hi:
#                 mid = lo + (hi - lo) // 2
#                 if a[mid] <= target:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             return lo

#         if not matrix:
#             return False
#         m, n = len(matrix), len(matrix[0])

#         for i in range(m):
#             n = binary_search(matrix[i], target, 0, n)
#             if n == 0:
#                 return False
#             if matrix[i][n - 1] == target:
#                 return True

#         return False


# # divide and conquer: O(nlogn) and O(logn)
# class Solution:
#     def searchMatrix(self, matrix, target):
#         m = len(matrix)
#         if m == 0:
#             return False
#         n = len(matrix[0])

#         def search_rec(left, right, up, down):
#             if left > right or up > down:
#                 return False
#             if target < matrix[up][left] or target > matrix[down][right]:
#                 return False
#             mid = left + (right - left) // 2
#             row = up
#             while row <= down and matrix[row][mid] <= target:
#                 if matrix[row][mid] == target:
#                     return True
#                 row += 1
#             return (search_rec(mid + 1, right, up, row - 1)
#                     or search_rec(left, mid - 1, row, down))

#         return search_rec(0, n - 1, 0, m - 1)


# search space reduction: O(m + n) and O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # starting from the left bottom corner, excluding invalid area during each step
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False


# @lc code=end
