#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counts = Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res
# @lc code=end

