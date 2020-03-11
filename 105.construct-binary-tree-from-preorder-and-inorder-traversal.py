#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.left: "Optional[TreeNode]" = None
        self.right: "Optional[TreeNode]" = None


# O(N) by master theorem and O(N) for storage of index
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {inorder[i]: i for i in range(len(inorder))}
        return self._buildTree(index, preorder, 0, inorder, 0, len(inorder) - 1)

    def _buildTree(self, index: Dict[int, int], preorder: List[int], pre_start: int,
                   inorder: List[int], in_start: int, in_end: int) -> Optional[TreeNode]:
        """Recursively build the tree.

        Parameters
        ----------
        index : Dict[int, int]
            {value of inorder: index of inorder}
        preorder : List[int]
        pre_start : int
            The root of the subtree.
        inorder : List[int]
        in_start : int
            Start position of the subarray in inorder to build the subtree.
        in_end : int
            End position of the subarray in inorder to build the subtree.

        Returns
        -------
        Optional[TreeNode]
        """
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


# @lc code=end
