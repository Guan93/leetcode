#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        lo, hi = 0, len(A)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid < len(A) - 1 and A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

# @lc code=end

