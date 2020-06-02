# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) and O(n)
# https://leetcode.com/problems/boundary-of-binary-tree/discuss/101280/Java(12ms)-left-boundary-left-leaves-right-leaves-right-boundary
# this answer has the same idea but handles the duplicates more elegantly
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        left_bound = self.find_path(root, left=True)
        right_bound = self.find_path(root, left=False)
        leaves = self.find_leaves(root)
        if left_bound:
            leaves = leaves[1:]
        if right_bound:
            leaves = leaves[:-1]
        return [root.val] + left_bound + leaves + right_bound[::-1]

    def find_leaves(self, root):
        res = []
        if not root.left and not root.right:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def find_path(self, root, left=True):
        res = []
        if left and not root.left or not left and not root.right:
            return res
        node = root.left if left else root.right
        res.append(node.val)
        while node.left or node.right:
            childs = [node.left, node.right] if left else [node.right, node.left]
            if childs[0]:
                node = childs[0]
            else:
                node = childs[1]
            res.append(node.val)
        return res