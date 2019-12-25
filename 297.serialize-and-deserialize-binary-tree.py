#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from typing import List, Optional

# class Codec:
#     # O(n) and O(n)
#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return None

#         def _dfs(node, preorder, inorder):
#             if not node:
#                 return None
#             preorder.append(str(node.val))
#             i = len(preorder) - 1
#             _dfs(node.left, preorder, inorder)
#             inorder.append(str(node.val))
#             index[i] = str(len(inorder) - 1)
#             _dfs(node.right, preorder, inorder)
#             return

#         preorder, inorder = [], []
#         index = {}
#         _dfs(root, preorder, inorder)
#         index = [index[i] for i in range(len(index))]
#         preorder, inorder, index = ' '.join(preorder), ' '.join(inorder), ' '.join(index)
#         return '\n'.join([preorder, inorder, index])

#     # O(n) and O(n)
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return None

#         preorder, inorder, index = data.split("\n")
#         preorder = [int(val) for val in preorder.split(' ')]
#         inorder = [int(val) for val in inorder.split(' ')]
#         index = [int(val) for val in index.split(' ')]
#         return self._buildTree(index, preorder, 0, inorder, 0, len(inorder) - 1)

#     def _buildTree(self, index: List[int], preorder: List[int], pre_start: int,
#                    inorder: List[int], in_start: int, in_end: int) -> Optional[TreeNode]:
#         if in_start > in_end:
#             return
#         if in_start == in_end:
#             return TreeNode(inorder[in_start])

#         root_val = preorder[pre_start]
#         inorder_index = index[pre_start]

#         root = TreeNode(root_val)
#         left_count = inorder_index - in_start
#         # right_count = in_end - inorder_index
#         root.left = self._buildTree(index, preorder, pre_start + 1, inorder, in_start,
#                                     inorder_index - 1)
#         root.right = self._buildTree(index, preorder, pre_start + left_count + 1, inorder,
#                                      inorder_index + 1, in_end)
#         return root

# preorder DFS: O(n) and O(n)
from collections import deque


class Codec:
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string.append('n')
            else:
                string.append(str(root.val))
                rserialize(root.left, string)
                rserialize(root.right, string)

        string = []
        rserialize(root, string)
        return ','.join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'n':
                l.popleft()
                return None

            root = TreeNode(l.popleft())
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_q = deque(data.split(','))
        root = rdeserialize(data_q)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
