#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        num_trees = [0] * (n + 1)
        num_trees[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                num_trees[i] += (num_trees[j - 1] * num_trees[i - j])
        return num_trees[n]


# @lc code=end
