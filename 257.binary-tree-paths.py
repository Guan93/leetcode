#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root):
            res = []
            if not root:
                return res
            left = dfs(root.left)
            right = dfs(root.right)
            if not left and not right:
                return [str(root.val)]
            for path in left:
                res.append(f"{root.val}->{path}")
            for path in right:
                res.append(f"{root.val}->{path}")
            return res
        res = dfs(root)
        return res


# @lc code=end

