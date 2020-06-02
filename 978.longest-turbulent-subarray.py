#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#


# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0

        lo = 0
        maxsize = 1

        for hi in range(1, len(A)):
            if A[hi] == A[hi - 1]:
                lo = hi
            elif hi == len(A) - 1 or (A[hi] - A[hi - 1]) * (A[hi + 1] - A[hi]) >= 0:
                maxsize = max(hi - lo + 1, maxsize)
                lo = hi

        return maxsize


# @lc code=end
