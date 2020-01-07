#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
        
# @lc code=end

