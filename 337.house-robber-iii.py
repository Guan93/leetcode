#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Tuple


class Solution:
    _maximum = 0

    def rob(self, root: TreeNode) -> int:
        prev2, prev1 = self._rob(root)
        return prev1

    def _rob(self, node: TreeNode) -> Tuple[int, int]:
        if not node:
            return 0, 0
        l_prev2, l_prev1 = self._rob(node.left)
        r_prev2, r_prev1 = self._rob(node.right)
        prev2 = l_prev1 + r_prev1
        prev1 = max(l_prev2 + r_prev2 + node.val, prev2)
        return prev2, prev1

    # more concise
    def rob(self, root: TreeNode) -> int:
        def _helper(root):
            if not root:
                return 0, 0

            left = _helper(root.left)
            right = _helper(root.right)
            return root.val + left[1] + right[1], max(left) + max(right)

        return max(_helper(root))


# @lc code=end
