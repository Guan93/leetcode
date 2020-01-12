#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cumsum = [0] * (n + 1)
        for i in reversed(range(n)):
            cumsum[i] = cumsum[i + 1] + piles[i]
        
        @lru_cache(None)
        def dp(i, m):
            if i >= n: return 0
            return cumsum[i] - min(dp(i + x, max(m, x)) for x in range(1, min(2 * m, n - i) + 1))
        return dp(0, 1)
# @lc code=end