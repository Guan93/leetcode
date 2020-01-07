#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) > 0:
                lo = mid + 1
            else:
                hi = mid
        return lo
# @lc code=end

