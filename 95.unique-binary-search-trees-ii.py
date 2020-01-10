#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    # # dp:
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     dp = defaultdict(list)

    #     for inter_len in range(1, n + 1):
    #         for start in range(n - inter_len + 1):
    #             for k in range(start, start + inter_len):
    #                 print(start, start + inter_len, (start, k), (k + 1, start + inter_len))
    #                 left, right = dp[(start, k)], dp[(k + 1, start + inter_len)]
    #                 if not left:
    #                     left = [None]
    #                 if not right:
    #                     right = [None]

    #                 for l in left:
    #                     for r in right:
    #                         root = TreeNode(k + 1)
    #                         root.left = l
    #                         root.right = r
    #                         dp[(start, start + inter_len)].append(root)
    #     return dp[(0, n)]

    # recursion
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self._generateTrees(start=0, end=n) if n > 0 else []

    def _generateTrees(self, start, end):
        if start == end:
            return [None]

        res = []
        for mid in range(start, end):
            for left in self._generateTrees(start, mid):
                for right in self._generateTrees(mid + 1, end):
                    root = TreeNode(mid + 1)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

# @lc code=end

