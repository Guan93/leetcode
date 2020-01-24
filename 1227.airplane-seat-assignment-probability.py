#
# @lc app=leetcode id=1227 lang=python3
#
# [1227] Airplane Seat Assignment Probability
#

# @lc code=start
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = [1.0] * (n + 1)
        cumsum = 0
        for i in range(2, n + 1):
            cumsum += dp[i - 1]
            dp[i] = cumsum / i
            # dp[i] = 1 / i + 1 / i * sum([dp[i + 1 - j] for j in range(2, i)])
        return dp[-1]
# @lc code=end

