class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, m = len(costs), len(costs[0])
        dp = [[0] * m for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(m):
                dp[i][j] = min(dp[i - 1][k] if k != j else float("inf") for k in range(m)) + costs[i - 1][j]
        return min(dp[-1])
