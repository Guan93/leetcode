#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        from collections import deque

        queue = deque([root])
        ended = False
        while queue:
            node = queue.popleft()
            if not node:
                ended = True
                continue
            if ended:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
# @lc code=end

