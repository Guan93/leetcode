#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        mapping = dict()
        for i, num in enumerate(nums):
            j = mapping.get(target - num)
            if j is not None:
                return [j, i]
            else:
                mapping[num] = i
