#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""This problem can make use of all the solutions in #1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs_preorder(root):
            if not root:
                return

            res.append(str(root.val))
            if root.left: dfs_preorder(root.left)
            if root.right: dfs_preorder(root.right)

        res = []
        dfs_preorder(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None

        preorder = [int(s) for s in data.split(',')]
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]):
        index = {inorder[i]: i for i in range(len(inorder))}
        return self._buildTree(index, preorder, 0, inorder, 0, len(inorder) - 1)

    def _buildTree(self, index, preorder, pre_start,
                   inorder, in_start, in_end):
        if in_start > in_end:
            return
        if in_start == in_end:
            return TreeNode(inorder[in_start])

        root_val = preorder[pre_start]
        inorder_index = index[root_val]

        root = TreeNode(root_val)
        left_count = inorder_index - in_start
        # right_count = in_end - inorder_index
        root.left = self._buildTree(index, preorder, pre_start + 1, inorder, in_start,
                                    inorder_index - 1)
        root.right = self._buildTree(index, preorder, pre_start + left_count + 1, inorder,
                                     inorder_index + 1, in_end)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

