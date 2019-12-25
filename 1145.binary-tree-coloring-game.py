#
# @lc app=leetcode id=1145 lang=python3
#
# [1145] Binary Tree Coloring Game
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]

        def _count(node):
            if not node:
                return 0
            l, r = _count(node.left), _count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return _count(root) / 2 < max(max(c), n - sum(c) - 1)

# @lc code=end
