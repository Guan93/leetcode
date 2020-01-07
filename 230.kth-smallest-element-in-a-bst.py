#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     def inorder_dfs(root, res):
    #         if not root:
    #             return
    #         inorder_dfs(root.left, res)
    #         res.append(root.val)
    #         inorder_dfs(root.right, res)
    #     res = []
    #     inorder_dfs(root, res)
    #     return res[k - 1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
# @lc code=end

