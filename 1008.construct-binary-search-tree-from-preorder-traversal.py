#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(nlogn) and O(n)
# inorder traverse the tree first and then use solution from #105
class Solution1:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(preorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        inorder = sorted(preorder)
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper()


# O(n) and O(h)
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution
class Solution2:
    idx = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self._bstFromPreorder(preorder, float("inf"))

    def _bstFromPreorder(self, preorder: List[int], upper) -> TreeNode:
        if self.idx == len(preorder) or preorder[self.idx] > upper:
            return None

        curr = preorder[self.idx]
        root = TreeNode(curr)
        self.idx += 1
        root.left = self._bstFromPreorder(preorder, curr)
        root.right = self._bstFromPreorder(preorder, upper)
        return root


# mono stack: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252722/Python-stack-solution-beats-100-on-runtime-and-memory
# O(n) and O(h)
class Solution3:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            else:
                while stack and val > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(val)
                stack.append(last.right)
        return root
# @lc code=end

