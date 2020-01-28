#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    # # O(n^2) (dominated by insertion) and O(1)
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     def bisect(a, target, lo, hi):
    #         while lo < hi:
    #             mid = lo + (hi - lo) // 2
    #             if a[mid] < target:
    #                 lo = mid + 1
    #             else:
    #                 hi = mid
    #         return lo

    #     def insert(a, target, idx):
    #         for i in reversed(range(idx, len(a) - 1)):
    #             a[i + 1] = a[i]
    #         a[idx] = target

    #     lo, hi = 0, len(nums1) - len(nums2)
    #     for target in nums2:
    #         lo = bisect(nums1, target, lo, hi)
    #         insert(nums1, target, lo)
    #         hi += 1

    # two-pointers: start from the end. O(m + n) and O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]

# @lc code=end

