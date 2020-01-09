#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations):
        if not citations:
            return 0
        lo, hi = 0, len(citations) + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if citations[-mid] >= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

# @lc code=end

