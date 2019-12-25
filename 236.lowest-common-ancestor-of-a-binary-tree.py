#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ans = 0

    # recursion O(n) and O(n)
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
    #                          q: 'TreeNode') -> 'TreeNode':
    #     self._dfs(root, p, q)
    #     return self.ans

    # def _dfs(self, node, p, q):
    #     if not node:
    #         return False
    #     left = self._dfs(node.left, p, q)
    #     right = self._dfs(node.right, p, q)
    #     mid = node == p or node == q

    #     if left + mid + right >= 2:
    #         self.ans = node
    #     return left or mid or right

    # # iteration using parent pointers O(n) and O(n)
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
    #                          q: 'TreeNode') -> 'TreeNode':
    #     parent = dict()
    #     stack = [root]

    #     # dfs to get all parent pointers
    #     while stack:
    #         node = stack.pop()
    #         if node.left:
    #             parent[node.left] = node
    #             stack.append(node.left)
    #         if node.right:
    #             parent[node.right] = node
    #             stack.append(node.right)

    #     # put all ancestors of p into a set
    #     ancestor_p = set()
    #     while p:
    #         ancestor_p.add(p)
    #         p = parent.get(p)

    #     # find the deepest ancestor of q that is also p's ancestor
    #     while q not in ancestor_p:
    #         q = parent.get(q)

    #     return q

    # simple
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


# @lc code=end
