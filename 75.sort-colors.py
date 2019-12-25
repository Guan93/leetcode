#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


# @lc code=start
class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     counts = [0, 0, 0]
    #     for num in nums:
    #         if num == 0:
    #             counts[0] += 1
    #         elif num == 1:
    #             counts[1] += 1
    #         else:
    #             counts[2] += 1

    #     j = 0
    #     for i in range(len(counts)):
    #         end = j + counts[i]
    #         while j < end:
    #             nums[j] = i
    #             j += 1

    def sortColors(self, nums: List[int]) -> None:
        p0 = 0  # right to the rightmost 0
        p2 = len(nums) - 1  # left to the leftmost 2
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


# @lc code=end
