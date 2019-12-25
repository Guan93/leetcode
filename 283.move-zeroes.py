#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    # time O(N), space O(N)
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     ans = []
    #     count = 0
    #     for num in nums:
    #         if num == 0:
    #             count += 1
    #         else:
    #             ans.append(num)
    #     ans += [0] * count
    #     for i in range(len(nums)):
    #         nums[i] = ans[i]

    # time O(N), space O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        last_nonzero_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_nonzero_at] = nums[i]
                last_nonzero_at += 1
        for i in range(last_nonzero_at, len(nums)):
            nums[i] = 0
        
# @lc code=end
