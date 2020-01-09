#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            elif nums[mid] >= nums[left]:  # left to mid is sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid + 1 to right is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# @lc code=end