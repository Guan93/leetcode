#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     min_price = float('inf')
    #     max_profit = 0
    #     for price in prices:
    #         if min_price > price:
    #             min_price = price
    #         elif price - min_price > max_profit:
    #             max_profit = price - min_price
    #     return max_profit

    # kadane's algo to find the max sum of subarray:
    # instead of looking at prices, we look at array of price changes and try to find
    # the subarray with largest sum
    def maxProfit(self, prices: List[int]) -> int:
        dp = max_profit = 0
        for i in range(1, len(prices)):
            dp = max(0, dp) + prices[i] - prices[i - 1]
            max_profit = max(max_profit, dp)
        return max_profit



# @lc code=end
