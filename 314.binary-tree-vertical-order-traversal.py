# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        res = deque()
        q = deque([(root, 0)])
        leftmost = 0

        while q:
            node, col = q.popleft()
            idx = col - leftmost
            if idx < 0:
                leftmost = col
                res.appendleft([node.val])
            elif idx >= len(res):
                res.append([node.val])
            else:
                res[idx].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return res