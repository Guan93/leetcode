#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs with hash table
# class Solution:
#     _depths = dict()

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return max(
#             max(
#                 self.diameterOfBinaryTree(root.left),
#                 self.diameterOfBinaryTree(root.right)),
#             self._get_depth(root.left) + self._get_depth(root.right))

#     def _get_depth(self, node: TreeNode) -> int:
#         if not node:
#             return 0
#         if node not in self._depths:
#             self._depths[node] = max(
#                 self._get_depth(node.left), self._get_depth(node.right)) + 1
#         return self._depths[node]


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._ans = 1

        def _depth(node):
            if not node:
                return 0
            L, R = _depth(node.left), _depth(node.right)
            # while calculating the subtree depth,
            # also record the maximum diameter encountered in the meantime
            self._ans = max(self._ans, L + R)
            return max(L, R) + 1

        _depth(root)
        return self._ans


# @lc code=end
