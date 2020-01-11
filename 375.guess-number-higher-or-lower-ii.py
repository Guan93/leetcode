#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#


# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                local_min = float("inf")
                for piv in range(start, start + length):
                    local_min = min(
                        local_min,
                        piv + 1 + max(dp[start][piv], dp[piv + 1][start + length]))
                dp[start][start + length] = local_min
        return dp[0][-1]


# @lc code=end
