#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # bfs: O(n) and O(n)
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque

        res = []
        if not root:
            return res
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if not queue or level != queue[0][1]:
                res.append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        return res

    # dfs: O(n) and O(h)
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(root, level):
            if not root:
                return

            if level == len(res):
                res.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        res = []
        dfs(root, 0)
        return res

# @lc code=end

