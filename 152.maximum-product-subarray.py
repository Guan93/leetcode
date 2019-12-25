#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = nums[0]
        global_max_prod = nums[0]
        for i in range(1, len(nums)):
            prod1 = max_prod * nums[i]
            prod2 = min_prod * nums[i]
            max_prod = max(max(prod1, prod2), nums[i])
            min_prod = min(min(prod1, prod2), nums[i])
            global_max_prod = max(max_prod, global_max_prod)
        return global_max_prod


# @lc code=end
