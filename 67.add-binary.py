#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a) - 1, len(b) - 1
        if p1 < p2:
            p1, p2 = p2, p1
            a, b = b, a
        res = []
        carry = 0
        while p1 >= 0:
            d1 = int(a[p1])
            d2 = int(b[p2]) if p2 >= 0 else 0
            carry, rem = divmod(d1 + d2 + carry, 2)
            res.append(str(rem))
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
# @lc code=end

