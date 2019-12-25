#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_i = max_global = nums[0]
        for i in range(1, len(nums)):
            max_i = max(max_i + nums[i], nums[i])
            max_global = max(max_i, max_global)
        return max_global


# @lc code=end
