#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * (mid + 1) / 2 <= n:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
# @lc code=end

