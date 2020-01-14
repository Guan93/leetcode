#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    # dp: O(n^2) and O(n^2)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[] for _ in range(len(nums) + 1)]

        res = []
        for i in range(1, len(nums) + 1):
            for j in reversed(range(i)):
                if (not dp[j] or nums[i - 1] % dp[j][-1] == 0) and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i - 1]]
            res = dp[i] if len(dp[i]) > len(res) else res
        return res
# @lc code=end
