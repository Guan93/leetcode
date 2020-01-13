#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(filter(lambda x: x > 0, [prices[i] - prices[i - 1]
                                            for i in range(1, len(prices))]))

# @lc code=end

