#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # s0: cooldown recovered, can buy or rest
        # s1: holding a stock
        # s2: just sold and need to cooldown
        s0, s1, s2 = ([0] * len(prices) for i in range(3))
        s0[0], s1[0], s2[0] = 0, -prices[0], -float("inf")
        for i in range(1, len(prices)):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s0[i - 1] - prices[i], s1[i - 1])
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[-1], s2[-1])


# @lc code=end
