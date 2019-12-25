#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

# # deque: O(n) and O(n)
# from collections import deque


# class Solution:
#     def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
#         n = len(nums)
#         if n == 0 or k == 0:
#             return []
#         if n == 1:
#             return nums

#         def clean_deque(i):
#             if deq and deq[0] == i - k:
#                 deq.popleft()
#             while deq and nums[i] > nums[deq[-1]]:
#                 deq.pop()

#         deq = deque()
#         for i in range(k):
#             clean_deque(i)
#             deq.append(i)
#         output = [nums[deq[0]]]

#         for i in range(k, n):
#             clean_deque(i)
#             deq.append(i)
#             output.append(nums[deq[0]])
#         return output


# dp: O(n) and O(n)
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right to build array left
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left to build array right
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output


# @lc code=end
