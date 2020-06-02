#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#


# @lc code=start
# bottom-up dp: O(kn) and O(k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # deal with edge case when k is extremely large
        # in this case we can take every positive daily profit
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        old_dp = [[-float("inf")] * (k + 1) for _ in range(2)]
        old_dp[0][0] = 0

        for i in range(len(prices)):
            dp = [[-float("inf")] * (k + 1) for _ in range(2)]
            for l in range(k + 1):
                dp[0][l] = max(old_dp[0][l], old_dp[1][l] + prices[i])
                dp[1][l] = old_dp[1][l]
                if l > 0:
                    dp[1][l] = max(old_dp[1][l], old_dp[0][l - 1] - prices[i])
            old_dp = dp

        return max(old_dp[0])


# @lc code=end
