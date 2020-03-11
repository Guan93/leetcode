#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(nums, curr):
#             if len(nums) == 0:
#                 res.append(curr)

#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i + 1:], curr + [nums[i]])

#         res = []
#         backtrack(nums, [])
#         return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])  # it is important to use slice [:] here to create a copy!
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        output = []
        backtrack()
        return output


# @lc code=end
