#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


# # brute force: O(n^3) and O(1)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         longest_streak = 0
#         for num in nums:
#             curr_num = num
#             curr_streak = 1

#             while curr_num + 1 in nums:
#                 curr_num += 1
#                 curr_streak += 1

#             longest_streak = max(longest_streak, curr_streak)
#         return longest_streak

# # sort and count: O(nlogn)

# hashtable O(n) and O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)

        return longest_streak

# @lc code=end
