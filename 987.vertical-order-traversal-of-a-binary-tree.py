#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        import heapq
        from collections import defaultdict

        def inorder_dfs(root, x, y):
            if not root:
                return
            inorder_dfs(root.left, x - 1, y - 1)
            heapq.heappush(queues[x], (-y, root.val))
            inorder_dfs(root.right, x + 1, y - 1)

        queues = defaultdict(list)
        inorder_dfs(root, 0, 0)
        leftmost, rightmost = min(queues.keys()), max(queues.keys())
        return [[val for _, val in queues[x]] for x in range(leftmost, rightmost + 1)]


# @lc code=end
