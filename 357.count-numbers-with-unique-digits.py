#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        s = 1
        if n == 0:
            return s
        prev = 9
        for i in range(1, n + 1):
            s += prev
            prev *= (10 - i)
        return s
# @lc code=end