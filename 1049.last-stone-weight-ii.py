#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    # # O(nw) and O(nw)
    # def lastStoneWeightII(self, stones: List[int]) -> int:
    #     s, s1 = sum(stones), 0
    #     n, w = s // 2, len(stones)
    #     dp = [[0] * (w + 1) for _ in range(n + 1)]
    #     for i in range(1, n + 1):
    #         for j in range(1, w + 1):
    #             if stones[j - 1] > i:
    #                 dp[i][j] = dp[i][j - 1]
    #             else:
    #                 dp[i][j] = max(dp[i][j - 1], dp[i - stones[j - 1]][j - 1] + stones[j - 1])
    #             s1 = max(s1, dp[i][j])
    #     return s - 2 * s1

    # O(ns) and O(s), where s = sum(A)
    def lastStoneWeightII(self, A):
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
            print(dp)
        return min(abs(sumA - i - i) for i in dp)

# @lc code=end
