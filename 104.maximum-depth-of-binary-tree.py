#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion O(n), O(height) worst case height is n and best case log(n)
    # def maxDepth(self, root: TreeNode) -> int:
    #     return self._max_height(root)

    # def _max_height(self, node: TreeNode) -> int:
    #     if not node:
    #         return 0
    #     left_height = self._max_height(node.left)
    #     right_height = self._max_height(node.right)
    #     return max(left_height, right_height) + 1
    
    # iteration
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = 0
        queue = [(root, 1)]
        while queue:
            node, curr_depth = queue.pop(0)
            max_depth = max(max_depth, curr_depth)
            if node.left:
                queue.append((node.left, curr_depth + 1))
            if node.right:
                queue.append((node.right, curr_depth + 1))
        return max_depth
# @lc code=end
