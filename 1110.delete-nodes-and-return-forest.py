from typing import List, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        root = self._dfs(root, to_delete, res)
        if root:
            res.append(root)
        return res

    def _dfs(self, node: TreeNode, to_delete: Set[int], res: List[TreeNode]):
        if node is None:
            return None
        node.left = self._dfs(node.left, to_delete, res)
        node.right = self._dfs(node.right, to_delete, res)
        if node.val in to_delete:
            if self.left: res.append(self.left)
            if self.right: res.append(self.right)
            node = None
        return node

    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res
