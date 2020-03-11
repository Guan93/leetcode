#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
# # top-down dp: O(n^3) and O(n^2)
# from functools import lru_cache

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         @lru_cache(None)
#         def _dp(left, right):
#             """
#             Return the maximum score obtainable in open interval (left, right)
#             """
#             if left + 1 == right:
#                 return 0

#             return max(nums[i] * nums[left] * nums[right] + _dp(left, i) + _dp(i, right)
#                        for i in range(left + 1, right))

#         nums = [1] + nums + [1]
#         return _dp(0, len(nums) - 1)


# bottom-up:
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for lo in range(n - length + 1):
                hi = lo + length - 1
                dp[lo][hi] = max([nums[lo] * nums[i] * nums[hi] + dp[lo][i] + dp[i][hi] for i in range(lo + 1, hi)])

        return dp[0][n - 1]


# @lc code=end
