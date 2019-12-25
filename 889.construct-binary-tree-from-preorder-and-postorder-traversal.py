#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# hashmap to locate numbers: O(n) and O(n)
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pre_pos, post_pos = dict(), dict()
        for i in range(len(pre)):
            pre_pos[pre[i]] = i
            post_pos[post[i]] = i

        def _helper(root_val):
            root = TreeNode(root_val)
            root_pre_pos = pre_pos[root_val]
            root_post_pos = post_pos[root_val]
            if (root_pre_pos < len(pre) - 1
                    and post_pos[pre[root_pre_pos + 1]] < post_pos[root_val]):
                root.left = _helper(pre[root_pre_pos + 1])
                if pre[root_pre_pos + 1] != post[root_post_pos - 1]:
                    root.right = _helper(post[root_post_pos - 1])
            return root
        return _helper(pre[0])

# genious: O(n) and O(depth)
class Solution:
    preIndex, posIndex = 0, 0
    def constructFromPrePost(self, pre, post):
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if (root.val != post[self.posIndex]):
            root.left = self.constructFromPrePost(pre, post)
        if (root.val != post[self.posIndex]):
            root.right = self.constructFromPrePost(pre, post)
        self.posIndex += 1
        return root

# @lc code=end
