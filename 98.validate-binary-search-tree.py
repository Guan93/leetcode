#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # recursion, O(n), O(n)
    # def isValidBST(self, root: TreeNode) -> bool:
    #     return self._helper(root, -float("inf"), float("inf"))

    # def _helper(self, node: TreeNode, lower: int, higher: int) -> bool:
    #     if not node:
    #         return True
    #     val = node.val
    #     return (val < higher and val > lower and self._helper(node.left, lower, val)
    #             and self._helper(node.right, val, higher))

    # dfs iteration, O(n), O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -float("inf"), float("inf"))]
        while stack:
            node, lower, higher = stack.pop()
            if not node:
                continue
            if node.val >= higher or node.val <= lower:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, higher))
        return True

    # recursive inorder traverse O(n), O(n)
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     res = []
    #     self._inorder_traverse(root, res)
    #     for i in range(len(res) - 1):
    #         if res[i] >= res[i + 1]:
    #             return False
    #     return True

    # def _inorder_traverse(self, node: TreeNode, res: List[int]):
    #     if not node:
    #         return node
    #     node.left = self._inorder_traverse(node.left, res)
    #     res.append(node.val)
    #     node.right = self._inorder_traverse(node.right, res)
    #     return node


# @lc code=end
