#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque

        res = 0
        curr_level = -1
        queue = deque([(root, 0, 1)])
        while queue:
            node, level, col = queue.popleft()
            if curr_level != level:
                leftmost = col
                curr_level = level
            res = max(res, col - leftmost + 1)
            if node.left:
                queue.append((node.left, level + 1, 2 * col - 1))
            if node.right:
                queue.append((node.right, level + 1, 2 * col))
        return res

# @lc code=end

