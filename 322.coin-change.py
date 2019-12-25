#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] <= amount else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * amount
        return self._coinChange(coins, amount, dp)

    def _coinChange(self, coins: List[int], rem: int, dp: List[int]) -> int:
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        cost = len(dp) + 1
        if dp[rem - 1] != 0:
            return dp[rem - 1]
        for coin in coins:
            res = self._coinChange(coins, rem - coin, dp)
            if res >= 0 and res < cost:
                cost = res + 1
        dp[rem - 1] = cost if cost <= len(dp) else -1
        return dp[rem - 1]


# @lc code=end
