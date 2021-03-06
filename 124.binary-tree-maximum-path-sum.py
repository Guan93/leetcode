#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion: O(n) and O(n) (we have to keep a recursion stack of size of the tree height,
# which is n in the worst case)


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self._global_max = - float("inf")

        def _helper(node):
            if not node:
                return 0
            left_max = max(_helper(node.left), 0)
            right_max = max(_helper(node.right), 0)
            self._global_max = max(self._global_max, left_max + right_max + node.val)
            return node.val + max(left_max, right_max)

        _helper(root)
        return self._global_max

# @lc code=end
