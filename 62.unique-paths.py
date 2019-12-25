#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
import math


class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     num_paths = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             num_paths[i][j] = num_paths[i - 1][j] + num_paths[i][j - 1]
    #     return num_paths[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))


# @lc code=end
