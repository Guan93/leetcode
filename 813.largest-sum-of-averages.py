#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

# @lc code=start
class Solution:
    # # O(k * n^2) and O(kn)
    # def largestSumOfAverages(self, A: List[int], K: int) -> float:
    #     dp = [[0] * K for _ in range(len(A) + 1)]
    #     cumsum = [0]
    #     for i in range(len(A)):
    #         cumsum.append(cumsum[-1] + A[i])

    #     for i in range(1, len(A) + 1):
    #         dp[i][0] = cumsum[i] / i
    #     for k in range(1, K):
    #         for i in range(1, len(A) + 1):
    #             dp[i][k] = max(max(dp[j][k - 1] + (cumsum[i] - cumsum[j]) / (i - j) for j in range(i)), dp[i][k - 1])
    #     return dp[-1][-1]

    # improve space complexity
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        cumsum, dp = [0], [0]
        for i in range(len(A)):
            cumsum.append(cumsum[-1] + A[i])
            dp.append(cumsum[-1] / (i + 1))

        for k in range(1, K):
            for i in reversed(range(1, len(A) + 1)):
                dp[i] = max(max(dp[j] + (cumsum[i] - cumsum[j]) / (i - j) for j in range(i)), dp[i])
        return dp[-1]


# @lc code=end