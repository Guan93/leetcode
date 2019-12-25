#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def _is_digit(self, c: str) -> bool:
        return ord('0') <= ord(c) <= ord('9')

    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        conv_started = False
        sign = 1
        res = 0

        for c in s:
            if not conv_started:
                if c == '+' or c == '-':
                    sign = 1 if c == '+' else -1
                    conv_started = True
                elif self._is_digit(c):
                    res = int(c)
                    conv_started = True
                elif c == ' ':
                    continue
                else:
                    break
            else:
                if not self._is_digit(c):
                    break
                if sign > 0 and res > INT_MAX / 10:
                    return INT_MAX
                if sign < 0 and - res < INT_MIN / 10:
                    return INT_MIN
                res = int(c) + res * 10

        return sign * res

# @lc code=end
