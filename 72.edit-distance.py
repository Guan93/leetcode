#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start

# https://leetcode.com/problems/edit-distance/discuss/25895/Step-by-step-explanation-of-how-to-optimize-the-solution-from-simple-recursion-to-DP


class Solution:
    # dp O(mn) and O(mn)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return m + n
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # init dp
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # compute dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]

    # O(mn) and O(n)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        curr = [0] * (n + 1)
        prev = list(range(n + 1))

        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(prev[j], curr[j - 1], prev[j - 1]) + 1
            for i in range(len(prev)):
                prev[i] = 0
            curr, prev = prev, curr
        return prev[-1]


# @lc code=end
