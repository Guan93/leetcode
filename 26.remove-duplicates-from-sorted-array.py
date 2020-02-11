#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        curr_num = None
        for num in nums:
            if num != curr_num:
                curr_num = nums[n] = num
                n += 1
        return n


# @lc code=end
