#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


# @lc code=start
class Solution:
    # dp bottom up: O(n^2) and O(n)
    def numTrees(self, n: int) -> int:
        num_trees = [0] * (n + 1)
        num_trees[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                num_trees[i] += (num_trees[j - 1] * num_trees[i - j])
        return num_trees[n]

    # recursion with memo: O(n^2) and O(n)
    def numTrees(self, n: int) -> int:
        def _helper(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            res = 0
            for i in range(n):
                res += _helper(i) * _helper(n - 1 - i)
            memo[n] = res
            return res

        memo = dict()
        return _helper(n)


# @lc code=end
