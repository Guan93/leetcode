#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        from collections import Counter

        dp = [[[0] * (len(strs) + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        counts = [Counter(s) for s in strs]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, len(strs) + 1):
                    count0, count1 = counts[k - 1]["0"], counts[k - 1]["1"]
                    if count0 > i or count1 > j:
                        dp[i][j][k] = dp[i][j][k - 1]
                    else:
                        dp[i][j][k] = max(dp[i][j][k - 1], dp[i - count0][j - count1][k - 1] + 1)
        return dp[-1][-1][-1]


# @lc code=end

