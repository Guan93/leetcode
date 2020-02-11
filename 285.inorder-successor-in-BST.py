# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive: O(N) and O(H)
class Solution:
    def __init__(self) -> None:
        self.n = 0
        self.has_finished = False

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = []
        self.inorder_dfs(root, p, res)
        return res[self.n] if self.n < len(res) else None

    def inorder_dfs(self, node, p, res):
        if len(res) == self.n + 1 or not node:
            return
        self.inorder_dfs(node.left, p, res)
        res.append(node)
        if node is p:
            self.n = len(res)
        self.inorder_dfs(node.right, p, res)



# iterative: O(N) and O(H)
class Solution:
    def inorderSuccessor(self, root, p):
        prev, stack = None, []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # pruning
            if prev is p:
                return root
            prev, root = root, root.right