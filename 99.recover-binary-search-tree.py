#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder_dfs(root):
            if not root:
                return

            inorder_dfs(root.left)

            if self.prev and root.val < self.prev.val:
                if not self.target:
                    self.target = self.prev
                else:
                    self.target.val, root.val = root.val, self.target.val
            self.prev = root

            inorder_dfs(root.right)

        self.prev = self.target = None

        inorder_dfs(root)
# @lc code=end

