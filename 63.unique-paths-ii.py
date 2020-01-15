#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])

        num_paths = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        num_paths[i][j] = 1
                    else:
                        num_paths[i][j] = ((num_paths[i - 1][j] if i > 0 else 0) +
                                           (num_paths[i][j - 1] if j > 0 else 0))
        return num_paths[-1][-1]


# @lc code=end
