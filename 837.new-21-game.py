#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start


class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W: return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K: Wsum += dp[i]
            if i - W >= 0: Wsum -= dp[i - W]
        return sum(dp[K:])

# class Solution:
#     def new21Game(self, N: int, K: int, W: int) -> float:
#         memo = dict()

#         def _helper(n_remain: int, k_remain: int) -> float:
#             if n_remain < k_remain:
#                 return 0.0
#             # n_remain >= k_remain
#             elif k_remain <= 0:
#                 return 1.0 if n_remain >= 0 else 0.0
#             # n_remain >= k_remian > 0
#             if (n_remain, k_remain) in memo:
#                 return memo[(n_remain, k_remain)]
#             prob = 0.0
#             for w in range(1, W + 1):
#                 prob += _helper(n_remain - w, k_remain - w) / W
#             memo[(n_remain, k_remain)] = prob
#             return prob

#         return _helper(N, K)

# @lc code=end
