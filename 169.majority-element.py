#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

class Solution:
    # hashmap
    # def majorityElement(self, nums: List[int]) -> int:
    #     counts = dict()
    #     for num in nums:
    #         if num in counts:
    #             counts[num] += 1
    #         else:
    #             counts[num] = 1
    #         if counts[num] > len(nums) // 2:
    #             return num

    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

# @lc code=end
