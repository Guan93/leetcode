#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[lo] + nums[hi] + nums[i]
                if abs(s - target) < abs(diff):
                    diff = s - target
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    return target
        return target + diff


# @lc code=end
