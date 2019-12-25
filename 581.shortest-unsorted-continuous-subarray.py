#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


# @lc code=start
class Solution:
    # Time O(nlog(n)), space O(n)
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     sorted_nums = [num for num in nums]
    #     sorted_nums.sort()
    #     for i in range(n):
    #         if nums[i] != sorted_nums[i]:
    #             break
    #     if i == n - 1:
    #         return 0
    #     for j in range(n - 1, i, -1):
    #         if nums[j] != sorted_nums[j]:
    #             break
    #     return j - i + 1

    # Time O(n), space O(n), using a stack
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l, r = len(nums) - 1, 0
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        if l == len(nums) - 1:
            return 0

        stack.clear()
        for i in range(len(nums) - 1, l - 1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1


# @lc code=end
