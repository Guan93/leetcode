#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    # O(nlogn) and O(n)
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        mid = (len(nums) + 1) // 2
        for i in range(mid):
            nums[2 * i] = sorted_nums[mid - 1 - i]

        for i in range(mid, len(nums)):
            nums[(i - mid) * 2 + 1] = sorted_nums[len(nums) - 1 - (i - mid)]

    def wiggleSort(self, nums):
        """
        Alternatively, we do not need to sort the nums;
        instead, we find the median first, which takes O(n) on average.
        """
        # TODO: O(n) + O(1)
        raise NotImplementedError

# @lc code=end

