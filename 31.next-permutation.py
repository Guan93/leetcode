#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        if i == 1 and nums[i - 1] >= nums[i]:
            nums = nums.reverse()
            return
        _min = float("inf")
        for j in range(len(nums) - 1, i - 1, -1):
            if nums[j] > nums[i - 1] and nums[j] < _min:
                _min = nums[j]
                k = j
        nums[i - 1], nums[k] = nums[k], nums[i - 1]
        nums[i:len(nums)] = nums[len(nums) - 1 : i - 1 : -1]
        
        
# @lc code=end
