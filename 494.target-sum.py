#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
class Solution:
    _count = 0

    # brute force
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     self._findTargetSumWays(nums, 0, 0, S)
    #     return self._count

    # def _findTargetSumWays(self, nums: List[int], i: int, sum: int, S: int) -> int:
    #     if i == len(nums):
    #         if sum == S:
    #             self._count += 1
    #     else:
    #         self._findTargetSumWays(nums, i + 1, sum + nums[i], S)
    #         self._findTargetSumWays(nums, i + 1, sum - nums[i], S)
    
    # recursion with memo
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        memo = [[-1] * (1001 + s) for _ in range(len(nums))]
        return self._findTargetSumWays(nums, 0, 0, S, memo)

    def _findTargetSumWays(self, nums: List[int], i: int, sum: int, S: int, memo) -> int:
        if i == len(nums):
            if sum == S:
                return 1
            else:
                return 0
        else:
            if memo[i][1000 + sum] != -1:
                return memo[i][1000 + sum]
            add = self._findTargetSumWays(nums, i + 1, sum + nums[i], S, memo)
            subtract = self._findTargetSumWays(nums, i + 1, sum - nums[i], S, memo)
            memo[i][1000 + sum] = add + subtract
            return memo[i][1000 + sum]
    
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # P: sum of numbers with positive sign
        # N: sum of numbers with negative sign
        # P - N = target => P = target + N # => 2 * P = target + N + P 
        #                => 2 * P = target + sum of nums
        # the problem is transformed to partition equal subset: pick numbers from num so
        # that they sum to target + sum of nums
        target = S + sum(nums)
        if (target & 1) == 1 or sum(nums) < S:
            return 0
        target = int(target / 2)

        dp = [1] + [0] * target
        for num in nums:
            i = target
            while i >= num:
                dp[i] += dp[i - num]
                i -= 1
        return dp[-1]


# @lc code=end
