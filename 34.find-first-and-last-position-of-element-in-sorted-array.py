#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def _binary_search(self, nums: List[int], target: int, sorting_left: bool = True) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if target < nums[mid] or (sorting_left and target == nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_range = [-1, -1]
        left_index = self._binary_search(nums, target, sorting_left=True)
        if left_index == len(nums) or nums[left_index] != target:
            return target_range
        target_range[0] = left_index
        target_range[1] = self._binary_search(nums, target, sorting_left=False) - 1
        return target_range

# @lc code=end
