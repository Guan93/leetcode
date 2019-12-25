#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

# trivial recursive solution
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self._inorder_traverse(root, res)
#         return res

#     def _inorder_traverse(self, node: TreeNode, res: List[int]) -> None:
#         if node:
#             self._inorder_traverse(node.left, res)
#             res.append(node.val)
#             self._inorder_traverse(node.right, res)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# @lc code=end
