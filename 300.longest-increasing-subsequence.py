#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    # dp: O(n^2) and O(n)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [1] * len(nums)
    #     len_LIS = 0
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #         len_LIS = max(len_LIS, dp[i])
    #     return len_LIS

    # dp and binary search
    # https://algorithmsandme.com/longest-increasing-subsequence-in-onlogn/
    # patience sorting https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        len_LIS = 0
        for num in nums:
            lo, hi = 0, len_LIS
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if dp[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            dp[lo] = num
            len_LIS = max(len_LIS, lo + 1)
        return len_LIS


# @lc code=end
