#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        p1 = 1
        p2 = 2
        if n == 1:
            return 1
        for i in range(2, n):
            p1, p2 = p2, p1 + p2
        return p2
# @lc code=end
