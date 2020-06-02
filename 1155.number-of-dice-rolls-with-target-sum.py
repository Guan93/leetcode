#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#


# @lc code=start
# top-down dp: O(d * f * target)
class Solution1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def dp(n, target):
            if target <= 0:
                return 0
            if n == 1:
                return int(target <= f)

            if (n, target) in memo:
                return memo[(n, target)]

            res = 0
            for i in range(1, f + 1):
                res += dp(n - 1, target - i)
            memo[(n, target)] = res % INT
            return memo[(n, target)]

        INT = 10**9 + 7
        memo = dict()
        return dp(d, target)


# bottom-up dp
class Solution2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        INT = 10**9 + 7

        dp = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(1, min(target, f) + 1):
            dp[1][i] = 1

        for i in range(2, d + 1):
            for j in range(1, target + 1):
                dp[i][j] = sum([dp[i - 1][j - k] if j - k > 0 else 0 for k in range(1, f + 1)]) % INT
        return dp[-1][-1]


# @lc code=end
