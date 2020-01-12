#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length
                dp[start][end] = max(piles[start] - dp[start + 1][end], 
                                     piles[end - 1] - dp[start][end - 1])
        return dp[0][-1] > 0
# @lc code=end
