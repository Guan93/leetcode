#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    # def wiggleMaxLength(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)
    #     start = 1
    #     while start < len(nums) and nums[start] == nums[start - 1]:
    #         start += 1
    #     if start == len(nums):
    #         return 1

    #     is_down, length = nums[start - 1] > nums[start], 2
    #     for i in range(start + 1, len(nums)):
    #         if (is_down and nums[i] > nums[i - 1]) or (not is_down and nums[i] < nums[i - 1]):
    #             length += 1
    #             is_down = not is_down
    #     return length

    # more explicit dp, same idea
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        down = up = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(down, up)

# @lc code=end

