#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


# @lc code=start
class Solution:
    # # brute force: O(n^2) and O(1)
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
    #     lo, hi = len(nums), 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] < nums[i]:
    #                 lo = min(i, lo)
    #                 hi = max(j, hi)
    #     return hi - lo + 1 if lo < hi else 0

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
        lo, hi = len(nums), 0

        left_stack = []
        for i in range(len(nums)):
            while left_stack and nums[left_stack[-1]] > nums[i]:
                lo = min(lo, left_stack.pop())
            left_stack.append(i)

        right_stack = []
        for j in reversed(range(len(nums))):
            while right_stack and nums[right_stack[-1]] < nums[j]:
                hi = max(hi, right_stack.pop())
            right_stack.append(j)

        return hi - lo + 1 if lo < hi else 0

    # time O(n), space O(1)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        unsorted_min = float("inf")
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                unsorted_min = min(unsorted_min, nums[i])

        unsorted_max = - float("inf")
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                unsorted_max = max(unsorted_max, nums[i])

        lo, hi = len(nums), 0
        for i in range(len(nums)):
            if nums[i] > unsorted_min:
                lo = i
                break
        for i in reversed(range(len(nums))):
            if nums[i] < unsorted_max:
                hi = i
                break
        return hi - lo + 1 if lo < hi else 0

# @lc code=end
