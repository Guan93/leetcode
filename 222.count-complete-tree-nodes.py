#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # O(n) and O(d) where d is a tree depth
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0


# binary search：two binary searches in total
# one for going down the tree and the other searching the last node in the last layer
# O(d^2) and O(1)
class Solution:
    def _compute_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def _exists(self, idx, d: int, node: TreeNode) -> bool:
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self._compute_depth(root)
        if d == 0:
            return 1

        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self._exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return (2**d - 1) + left


# @lc code=end
