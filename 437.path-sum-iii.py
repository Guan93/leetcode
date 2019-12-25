#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# brute force: space O(n), time worst O(n^2) when no branching, O(nlogn) when balanced
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         if not root:
#             return 0
#         return (self._pathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(
#             root.right, sum))

#     def _pathSum(self, node: TreeNode, curr_sum: int) -> int:
#         count = 0
#         if not node:
#             return count
#         if curr_sum == node.val:
#             count += 1
#         count += (self._pathSum(node.left, curr_sum - node.val) + self._pathSum(
#             node.right, curr_sum - node.val))
#         return count

# dfs with hash table, O(n) and O(n)
import collections


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        counts = collections.defaultdict(int)
        counts[0] = 1
        return self._dfs(root, sum, 0, counts)

    def _dfs(self, node: TreeNode, sum: int, curr_sum: int,
             counts: collections.defaultdict):
        total = 0
        if not node:
            return total
        curr_sum = curr_sum + node.val
        # if there exists old_sums in counts that satisfy old_sum = curr_sum - sum,
        # then we have found a path
        total += counts[curr_sum - sum]
        # add curr_sum to counts for subtrees
        counts[curr_sum] += 1
        total += (self._dfs(node.left, sum, curr_sum, counts) +
                  self._dfs(node.right, sum, curr_sum, counts))
        # after visiting all the subtrees, subtract curr_sum in counts by one since we
        # are going back up the tree
        counts[curr_sum] -= 1
        return total


# @lc code=end
