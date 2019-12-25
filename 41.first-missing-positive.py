#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start

# # O(n) and O(n)
# from collections import Counter

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         count = Counter()
#         for num in nums:
#             if num <= 0 or num > len(nums):
#                 continue
#             count[num] += 1

#         for i in range(1, len(nums) + 1):
#             if count[i] == 0:
#                 return i
#         return len(nums) + 1


# O(n) and O(1)
class Solution:
    def firstMissingPositive(self, nums):
        """
        Use index as a hash key and number sign as a presense detector.
        For example, if nums[1] is negative, it means that number '1' is
        present in the array; if nums[2] is positive, it means that number
        '2' is missing.
        """
        if 1 not in nums:
            return 1

        n = len(nums)
        # replace negative and numbers greater than n with 1 so that
        # only positive numbers are in the array.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


# @lc code=end
