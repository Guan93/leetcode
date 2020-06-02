#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        def helper(digit, ten, five, one):
            if digit == 4:
                res = one + five
            elif digit == 9:
                res = one + ten
            else:
                half, rem = divmod(digit, 5)
                res = half * five + rem * one

            return res

        if not (0 < num < 4000):
            return ""
        res = ""
        thousand, rem = divmod(num, 1000)
        res += thousand * "M"

        hundred, rem = divmod(rem, 100)
        res += helper(hundred, "M", "D", "C")
        ten, rem = divmod(rem, 10)
        res += helper(ten, "C", "L", "X")
        res += helper(rem, "X", "V", "I")


# @lc code=end
