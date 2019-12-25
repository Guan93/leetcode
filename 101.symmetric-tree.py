#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    # recursion
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     return self._is_mirror(root, root)

    # def _is_mirror(self, left_node: TreeNode, right_node: TreeNode) -> bool:
    #     if not left_node and not right_node:
    #         return True
    #     if not left_node or not right_node:
    #         return False
    #     return (left_node.val == right_node.val and
    #             self._is_mirror(left_node.right, right_node.left) and
    #             self._is_mirror(right_node.left, left_node.right))

    # DFS iteration
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     stack = []
    #     stack.append(root)
    #     stack.append(root)

    #     while stack:
    #         node1 = stack.pop()
    #         node2 = stack.pop()
    #         if not node1 and not node2:
    #             continue
    #         if not node1 or not node2 or node1.val != node2.val:
    #             return False
    #         stack.append(node1.left)
    #         stack.append(node2.right)
    #         stack.append(node1.right)
    #         stack.append(node2.left)
    #     return True

    # BFS iteration
    def isSymmetric(self, root: TreeNode) -> bool:

        q = queue.Queue()
        q.put(root)
        q.put(root)

        while not q.empty():
            node1 = q.get()
            node2 = q.get()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            q.put(node1.left)
            q.put(node2.right)
            q.put(node1.right)
            q.put(node2.left)
        return True


# @lc code=end
