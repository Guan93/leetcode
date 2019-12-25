#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        self._pathSum(root, sum, [], paths)
        return paths

    def _pathSum(self, node: TreeNode, sum: int, path: List[int],
                 paths: List[List[int]]) -> None:
        if not node:
            return
        if not node.left and not node.right:
            if sum == node.val:
                paths.append(path + [node.val])
            return
        self._pathSum(node.left, sum - node.val, path + [node.val], paths)
        self._pathSum(node.right, sum - node.val, path + [node.val], paths)


# @lc code=end
