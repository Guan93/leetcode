#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    # binary search, time O(nlog(n)), space O(1)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     low = 1
    #     high = len(nums) - 1
    #     while low < high:
    #         mid = low + (high - low) // 2
    #         count = 0
    #         for num in nums:
    #             if num <= mid:
    #                 count += 1
    #         # if count > mid, the duplicate value must be in [1, 2, ..., mid].
    #         if count > mid:
    #             high = mid
    #         # otherwise, the duplicate value must be in the other half.
    #         else:
    #             low = mid + 1
    #     return low

    # cycle detect: problem #142
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        pt1 = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                pt2 = slow
                while pt1 != pt2:
                    pt1 = nums[pt1]
                    pt2 = nums[pt2]
                return pt1
# @lc code=end
