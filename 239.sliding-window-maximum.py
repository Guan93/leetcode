#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

# # deque: O(n) and O(n)
# from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        from collections import deque

        dq = deque()
        res = []

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# dp: O(n) and O(n)
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums:
            return []

        k = min(k, len(nums))
        left = [0] * len(nums)
        right = [0] * len(nums)

        for start in range(len(nums)):
            if start % k == 0:
                left[start] = nums[start]
            else:
                left[start] = max(left[start - 1], nums[start])

        for end in reversed(range(len(nums))):
            if end % k == k - 1 or end == len(nums) - 1:
                right[end] = nums[end]
            else:
                right[end] = max(right[end + 1], nums[end])

        res = []
        for start in range(len(nums) - k + 1):
            end = start + k - 1
            res.append(max(left[end], right[start]))

        return res


# monoqueue implementation: production version
from collections import deque


class Monoqueue:
    def __init__(self):
        # each element is a pair
        # first: the actual value
        # second: how many elements were deleted between it and the one before it
        self.m_deque = deque()

    def push(self, val):
        count = 0
        while self.m_deque and self.m_deque[-1][0] < val:
            count += self.m_deque[-1][1] + 1
            self.m_deque.pop()
        self.m_deque.append([val, count])

    def max(self):
        return self.m_deque[0][0]

    def pop(self):
        if self.m_deque[0][1] > 0:
            self.m_deque[0][1] -= 1
            return
        self.m_deque.popleft()


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        k = min(k, len(nums))
        mq = Monoqueue()

        for i in range(k - 1):
            mq.push(nums[i])

        res = []
        for i in range(max(k - 1, 0), len(nums)):
            mq.push(nums[i])
            res.append(mq.max())
            mq.pop()
        return res


# @lc code=end
