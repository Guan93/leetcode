#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # iteration BFS: O(n) and O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        small, large = min(p.val, q.val), max(p.val, q.val)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if (node.val >= small and node.val <= large):
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # iteration O(n) and O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        node = root
        small, large = min(p.val, q.val), max(p.val, q.val)

        while node:
            if node.val > large:
                node = node.left
            elif node.val < small:
                node = node.right
            else:
                return node


# @lc code=end
