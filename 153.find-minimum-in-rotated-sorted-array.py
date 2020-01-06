#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[0] <= nums[mid] and nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


# @lc code=end
