#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
class Solution:
    # O(n^2) and O(n^2)
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        cumsum = [0]
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            dp[i][i + 1] = nums[i]
            cumsum.append(cumsum[-1] + nums[i])

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length
                dp[start][end] = cumsum[end] - cumsum[start] - min(dp[start + 1][end], dp[start][end - 1])

        return dp[0][-1] * 2 >= sum(nums)
# @lc code=end

