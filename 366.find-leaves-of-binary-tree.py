# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root:
                return -1

            level = max(dfs(root.left), dfs(root.right)) + 1
            if level < len(res):
                res[level].append(root.val)
            elif level == len(res):
                res.append([root.val])

            return level

        res = []
        dfs(root)
        return res
