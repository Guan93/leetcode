#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(|s| * |t|) and O(H) where H is the height of s
class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isEqual(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isEqual(self, s, t):
        if not (s and t):
            return s is None and t is None
        return (s.val == t.val and self.isEqual(s.left, t.left)
                and self.isEqual(s.right, t.right))


# @lc code=end
