#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

# # O(n) and O(1)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         median_idx = (m + n) // 2
#         odd = (m + n) % 2 == 1
#         i = j = k = 0
#         curr = prev = 0
#         while i < m or j < n:
#             prev = curr
#             if i < m and j < n:
#                 if nums1[i] < nums2[j]:
#                     curr = nums1[i]
#                     i += 1
#                 else:
#                     curr = nums2[j]
#                     j += 1
#             elif i == m:
#                 curr = nums2[j]
#                 j += 1
#             else:
#                 curr = nums1[i]
#                 i += 1
#             k += 1
#             if k == median_idx + 1:
#                 return curr if odd else (prev + curr) / 2
#         return 0


# O(log(min(m, n))) and O(1)
# https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a, len_b = len(nums1), len(nums2)
        if len_a > len_b:
            len_a, len_b, nums1, nums2 = len_b, len_a, nums2, nums1
        len_half = (len_a + len_b + 1) // 2
        is_odd = (len_a + len_b) % 2 == 1
        if len_a == 0:
            return (nums2[len_half - 1] if is_odd else
                    (nums2[len_half - 1] + nums2[len_half]) / 2)
        lo, hi = max(0, len_half - len_b), min(len_a, len_half)

        while lo <= hi:
            count_a = lo + (hi - lo) // 2
            count_b = len_half - count_a

            if count_a > 0 and nums1[count_a - 1] > nums2[count_b]:
                hi = count_a - 1
            elif count_a < len_a and nums2[count_b - 1] > nums1[count_a]:
                lo = count_a + 1
            else:
                if count_a == 0:
                    left_end = nums2[count_b - 1]
                elif count_b == 0:
                    left_end = nums1[count_a - 1]
                else:
                    left_end = max(nums2[count_b - 1], nums1[count_a - 1])

                if is_odd:
                    return left_end
                if count_a == len_a:
                    right_start = nums2[count_b]
                elif count_b == len_b:
                    right_start = nums1[count_a]
                else:
                    right_start = min(nums1[count_a], nums2[count_b])
                return (left_end + right_start) / 2
        return -1


# @lc code=end
