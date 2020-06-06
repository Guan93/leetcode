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



# @lc code=end

