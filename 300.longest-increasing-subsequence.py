#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    # dp
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     # dp[i]: maximum length of the longest increasing subsequence
    #     #        containing element nums[i]
    #     dp = [1] * n
    #     dp[0] = 1
    #     len_LIS = 0
    #     for i in range(n):
    #         maxval = 1
    #         for k in range(i):
    #             if nums[i] > nums[k]:
    #                 maxval = max(dp[k] + 1, maxval)
    #         dp[i] = maxval
    #         len_LIS = max(len_LIS, maxval)
    #     return len_LIS

    # dp and binary search
    # https://algorithmsandme.com/longest-increasing-subsequence-in-onlogn/
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        max_length = 0
        for num in nums:
            i, j = 0, max_length
            # binary search
            while i != j:
                m = int((i + j) / 2)
                if num < dp[m]:
                    j = m
                elif num > dp[m]:
                    i = m + 1
                else:
                    i = m
                    break
            dp[i] = num
            max_length = max(max_length, i + 1)
        return max_length


# @lc code=end
