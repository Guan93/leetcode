#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def _helper(clip, curr_len):
            if clip > n - curr_len:
                return float("inf")
            if clip == n - curr_len:
                return 1
            return min(1 + _helper(clip, curr_len + clip), 2 + _helper(curr_len, 2 * curr_len))
        if n <= 1:
            return 0
        return _helper(1, 1) + 1
# @lc code=end

