class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        Let dp[n] denote the total number of possible ways at n.
        To paint the fence at n, we have two choices:
           1. paint it with the same color as n - 1
           2. paint it with a different color
            dp[n] = diff[n] + same[n]
        For case 2, it is obvious that:
            diff[n] = dp[n - 1] * (k - 1)
        For case 1, we can only use the same color when colors at n - 1 and n - 2 are different:
            same[n] = diff[n - 1] = dp[n - 2] * (k - 1)
        Therefore,
            dp[n] = same[n] + diff[n] = (dp[n - 1] + dp[n - 2]) * (k - 1)
        """
        prev, curr = k, k ** 2
        if n == 1:
            return prev
        for i in range(3, n + 1):
            prev, curr = curr, (k - 1) * (curr + prev)
        return curr
