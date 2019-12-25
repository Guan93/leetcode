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
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                if left + 1 == right:
                    dp[left][right] = 0
                else:
                    dp[left][right] = max(
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                        for i in range(left + 1, right))
        return dp[0][n - 1]


# @lc code=end
