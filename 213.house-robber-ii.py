#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def _rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        for num in nums:
            prev1, prev2 = max(prev1, prev2 + num), prev1
        return prev1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))


# @lc code=end
