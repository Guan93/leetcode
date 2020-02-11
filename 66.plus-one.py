#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        from collections import deque

        res = deque()
        i = len(digits) - 1
        prev = 0
        while i >= 0:
            if prev == 0:
                prev = (digits[i] + 1) % 9
                print(prev)
            else:
                prev = digits[i]
            i -= 1
            print(res)
        if prev == 0:
            res.appendleft(1)
        return res

# @lc code=end

