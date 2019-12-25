#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start


# use function from #1143 to find the longest common subsequence: O(mn) and O(mn)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        maxlens = self.longestCommonSubsequence(word1, word2)       
        return len(word1) + len(word2) - 2 * maxlens

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i - 1][j - 1] if i > 0 and j > 0 else 0) + 1
                else:
                    dp[i][j] = max(dp[i][j - 1] if j > 0 else 0, dp[i - 1][j] if i > 0 else 0)
        return dp[-1][-1]
# @lc code=end
