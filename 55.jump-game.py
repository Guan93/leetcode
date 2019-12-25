#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if reachable - i <= nums[i]:
                reachable = i
        return reachable == 0

# @lc code=end
