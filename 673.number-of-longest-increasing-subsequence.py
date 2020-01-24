#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    # dp: O(n^2) and O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        counts = [1] * len(nums)
        max_length = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        counts[i] += counts[j]
                    elif length[i] < length[j] + 1:
                        counts[i] = counts[j]
                        length[i] = length[j] + 1
                        max_length = max(max_length, length[i])
        return sum([counts[i] for i in range(len(counts)) if length[i] == max_length])

# @lc code=end

