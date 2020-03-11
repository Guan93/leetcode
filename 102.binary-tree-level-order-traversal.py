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
        from collections import deque

        res = []
        if not root:
            return res
        queue = deque([(root, 0)])

        curr_level, curr_list = 0, []
        while queue:
            node, level = queue.popleft()
            if curr_level == level:
                curr_list.append(node.val)
            else:
                res.append(curr_list)
                curr_level, curr_list = level, [node.val]
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res.append(curr_list)

        return res


# @lc code=end
