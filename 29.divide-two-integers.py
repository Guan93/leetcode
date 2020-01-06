#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        quotient = 0
        while abs_dividend >= abs_divisor:
            i, tmp_divisor = 1, abs_divisor
            while abs_dividend >= tmp_divisor:
                abs_dividend -= tmp_divisor
                quotient += i
                tmp_divisor += tmp_divisor
                i += i
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            quotient = 0 - quotient
        return max(min(2**31 - 1, quotient), - 2**31)

# @lc code=end