#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num // 2 + 2
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid < num:
                lo = mid + 1
            else:
                hi = mid
        return lo * lo == num
# @lc code=end

