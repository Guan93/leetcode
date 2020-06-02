"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# inorder dfs with a list to store
# O(n) and O(n)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)

        inorder = []
        if not root:
            return None
        dfs(root)
        n = len(inorder)
        for i in range(n):
            prev, nxt = (i - 1) % n, (i + 1) % n
            inorder[i].left = inorder[prev]
            inorder[i].right = inorder[nxt]
        return inorder[0]

# inorder dfs without extra list
# O(n) and O(h)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node
                last = node
                # right
                helper(node.right)

        if not root:
            return None

        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first