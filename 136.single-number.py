#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start


class Solution:
    # hash table
    # def singleNumber(self, nums: List[int]) -> int:
    #     counts = dict()
    #     for num in nums:
    #         if num in counts:
    #             counts.pop(num)
    #         else:
    #             counts[num] = 1
    #     return counts.popitem()[0]

    # math
    # def singleNumber(self, nums: List[int]) -> int:
    #     return 2 * sum(set(nums)) - sum(nums)

    # bit manipulation
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

# @lc code=end
