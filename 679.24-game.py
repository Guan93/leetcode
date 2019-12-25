#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
import itertools


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def _equal(x, y):
            return abs(x - y) < 1e-6

        def _helper(nums):
            if len(nums) == 2:
                return (_equal(nums[0] + nums[1], 24) or _equal(nums[0] - nums[1], 24)
                        or _equal(nums[0] * nums[1], 24)
                        or (_equal(nums[0] / nums[1], 24) if nums[1] != 0 else False))
            for i in range(len(nums) - 1):
                if (_helper(nums[:i] + (nums[i] + nums[i + 1], ) + nums[i + 2:])
                        or _helper(nums[:i] + (nums[i] - nums[i + 1], ) + nums[i + 2:])
                        or _helper(nums[:i] + (nums[i] * nums[i + 1], ) + nums[i + 2:])
                        or (_helper(nums[:i] + (nums[i] / nums[i + 1], ) + nums[i + 2:])
                            if nums[i + 1] != 0 else False)):
                    return True
            return False

        for perm in itertools.permutations(nums):
            if _helper(perm):
                return True
        return False


# @lc code=end
