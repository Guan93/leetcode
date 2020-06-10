#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ...

    def convert_digit(self, digit: str) -> int:
        return ord(digit) - ord('0')

    def add(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        if i < j:
            i, j = j, i
            num1, num2 = num2, num1

        carry = 0
        res = []
        while i >= 0:
            d1 = self.convert_digit(num1[i])
            d2 = self.convert_digit(num2[j]) if j >= 0 else 0
            carry, d = divmod(d1 + d2 + carry, 10)
            res.append(str(d))
            i, j = i - 1, j - 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])





# @lc code=end

