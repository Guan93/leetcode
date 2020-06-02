#
# @lc app=leetcode id=1223 lang=python3
#
# [1223] Dice Roll Simulation
#

# @lc code=start


# dp: O(36n) and O(6n)
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        DIV = 10**9 + 7
        dp = [[0] * 6 for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1

        for k in range(1, n):
            for i in range(6):
                roll_max = rollMax[i]
                dp[k][i] += sum(dp[k - 1][j] for j in range(6)) % DIV
                if k - roll_max - 1 >= 0:
                    dp[k][i] -= sum(dp[k - roll_max - 1][j]
                                    for j in range(6) if j != i) % DIV
                elif k - roll_max == 0:
                    dp[k][i] -= 1

        return sum(dp[n - 1]) % DIV


# @lc code=end
