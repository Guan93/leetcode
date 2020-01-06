#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    # binary
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 1, x // 2 + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

# @lc code=end
