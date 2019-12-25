#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#


# @lc code=start
import collections


class Solution:
    # O(n^2)
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     for i in range(len(nums)):
    #         s = 0
    #         for j in range(i, len(nums)):
    #             s += nums[j]
    #             if s == k:
    #                 count += 1
    #     return count

    # O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        counter = collections.Counter()
        counter[0] = 1
        for num in nums:
            s += num
            # if there is a previous cumsum with value s - k,
            # current cumsum minus previous one makes a subarray which sums to k
            count += counter[s - k]
            counter[s] += 1
        return count


# @lc code=end
