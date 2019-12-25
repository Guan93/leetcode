#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            if not level:
                break
            queue.append([])
            vals = []
            for node in level:
                if node:
                    vals.append(node.val)
                    queue[-1].append(node.left)
                    queue[-1].append(node.right)
            if vals:
                ans.append(vals)

        return ans


# @lc code=end
