#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# trivial inorder dfs, takes O(n) space
class BSTIterator:
    def __init__(self, root: TreeNode):
        self._inorder_array = []
        self._next_idx = 0
        self._inorder_dfs(root)

    def _inorder_dfs(self, root):
        if not root:
            return

        self._inorder_dfs(root.left)
        self._inorder_array.append(root.val)
        self._inorder_dfs(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            next_val = self._inorder_array[self._next_idx]
            self._next_idx += 1
            return next_val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._next_idx < len(self._inorder_array)


# use stack to iteratively do inorder dfs so that we can freely pause and resume
# space O(H)
class BSTIterator:
    def __init__(self, root) -> None:
        self._stack = []
        self._traverse_leftmost(root)

    def _traverse_leftmost(self, root):
        while root:
            self._stack.append(root)
            root = root.left

    def next(self):
        if not self.hasNext():
            return None
        top = self._stack.pop()
        self._traverse_leftmost(top.right)
        return top.val

    def hasNext(self):
        return len(self._stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

