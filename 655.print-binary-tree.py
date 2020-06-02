#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# two pass: O(n) and O(h)
class Solution1:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_shape(root):
            if not root:
                return 0, 0
            l_width, l_height = get_shape(root.left)
            r_width, r_height = get_shape(root.right)
            width = 1 + 2 * max(l_width, r_width)
            height = 1 + max(l_height, r_height)
            return width, height

        def fill_value(lo, hi, level, root):
            if not root:
                return
            mid = (lo + hi) // 2
            res[level][mid] = str(root.val)
            fill_value(lo, mid - 1, level + 1, root.left)
            fill_value(mid + 1, hi, level + 1, root.right)

        width, height = get_shape(root)
        res = [[""] * width for _ in range(height)]
        fill_value(0, width - 1, 0, root)
        return res

# width can be derived from height
class Solution2:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_height(root):
            if not root:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))

        def fill_value(lo, hi, level, root):
            if not root:
                return
            mid = (lo + hi) // 2
            res[level][mid] = str(root.val)
            fill_value(lo, mid - 1, level + 1, root.left)
            fill_value(mid + 1, hi, level + 1, root.right)

        height = get_height(root)
        width = 2 ** height - 1
        res = [[""] * width for _ in range(height)]
        fill_value(0, width - 1, 0, root)
        return res

# @lc code=end

