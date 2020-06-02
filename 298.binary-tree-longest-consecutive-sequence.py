# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def helper(root, curr_len):
            nonlocal max_len
            max_len = max(max_len, curr_len)
            for node in [root.left, root.right]:
                if not node:
                    continue
                if node.val == root.val + 1:
                    helper(node, curr_len + 1)
                else:
                    helper(node, 1)

        if not root:
            return 0
        max_len = 0
        helper(root, 1)
        return max_len
