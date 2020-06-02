# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return True
            left = helper(root.left) and (not root.left or root.left.val == root.val)
            right = helper(root.right) and (not root.right or root.right.val == root.val)
            if left and right:
                self.count += 1
                return True
            return False

        self.count = 0
        helper(root)
        return self.count