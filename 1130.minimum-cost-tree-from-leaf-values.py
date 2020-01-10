#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
class Solution:
    # dp: O(n^3) and O(n^2)
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_vals = [[1] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            local_max = 0
            for j in range(i, n):
                if arr[j] > local_max:
                    local_max = arr[j]
                max_vals[i][j + 1] = local_max

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                min_cost = float("inf")
                for k in range(j + 1, j + i):
                    min_cost = min(min_cost, dp[j][k] + dp[k][j + i] + max_vals[j][k] * max_vals[k][j + i])
                dp[j][j + i] = min_cost if min_cost < float("inf") else dp[j][j + i]
        return dp[0][-1]

# @lc code=end
