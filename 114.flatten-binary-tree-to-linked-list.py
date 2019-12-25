#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # with a helper function: first left then right
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if root:
    #         self._helper(root)

    # def _helper(self, node: TreeNode) -> TreeNode:
    #     """
    #     Return the tail node after rearranging subtree node.
    #     """
    #     if not node.left and not node.right:
    #         return node
    #     tail = self._helper(node.left) if node.left else node
    #     node.right, node.left, tail.right = node.left, None, node.right
    #     tail = self._helper(tail.right) if tail.right else tail
    #     return tail

    # without a helper function, reverse traverse: first right then left
    def __init__(self) -> None:
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


# @lc code=end
