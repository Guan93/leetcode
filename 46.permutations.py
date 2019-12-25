#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = []
#         self._helper(nums, [], ans)
#         return ans

#     def _helper(self, nums: List[int], bt: List[int], ans: List[List[int]]) -> None:
#         if len(nums) == 1:
#             ans.append(bt + nums)
#             return

#         for i in range(len(nums)):
#             tmp = [num for num in nums]
#             tmp.pop(i)
#             self._helper(tmp, bt + [nums[i]], ans)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        output = []
        backtrack()
        return output


# @lc code=end
