#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for divisor in [2, 3, 5]:
            while num % divisor == 0:
                num = num // divisor
        return num == 1

# @lc code=end

