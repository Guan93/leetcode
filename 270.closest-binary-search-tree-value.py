# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float("inf")
        while root:
            res = root.val if abs(root.val - target) < abs(res - target) else res
            if root.val == target:
                break
            elif root.val > target:
                root = root.left
            else:
                root = root.right
        return res