#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        while p1 >= 0 or p2 >= 0:
            d1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            res = f"{digit}{res}"
            p1, p2 = p1 - 1, p2 - 1
        if carry > 0:
            res = f"{carry}{res}"
        return res


# @lc code=end
