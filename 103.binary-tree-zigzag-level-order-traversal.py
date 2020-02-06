#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # # bfs: O(n) and O(n)
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     from collections import deque

    #     res = []
    #     curr_res = []
    #     if not root:
    #         return res

    #     queue = deque([(root, 0)])
    #     curr_level = 0

    #     while queue:
    #         node, level = queue.popleft()
    #         if curr_level == level:
    #             curr_res.append(node.val)
    #         else:
    #             if curr_level % 2 == 1:
    #                 res.append(curr_res[::-1])
    #             else:
    #                 res.append(curr_res)
    #             curr_res = [node.val]
    #             curr_level = level

    #         if node.left:
    #             queue.append((node.left, curr_level + 1))
    #         if node.right:
    #             queue.append((node.right, curr_level + 1))
    #     if curr_level % 2 == 1:
    #         res.append(curr_res[::-1])
    #     else:
    #         res.append(curr_res)
    #     return res

    # # same bfs: can use a delimiter to make code more concise
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     from collections import deque

    #     ret = []
    #     level_list = deque()
    #     if root is None:
    #         return []
    #     # start with the level 0 with a delimiter
    #     node_queue = deque([root, None])
    #     is_order_left = True

    #     while len(node_queue) > 0:
    #         curr_node = node_queue.popleft()

    #         if curr_node:
    #             if is_order_left:
    #                 level_list.append(curr_node.val)
    #             else:
    #                 level_list.appendleft(curr_node.val)

    #             if curr_node.left:
    #                 node_queue.append(curr_node.left)
    #             if curr_node.right:
    #                 node_queue.append(curr_node.right)
    #         else:
    #             # we finish one level
    #             ret.append(level_list)
    #             # add a delimiter to mark the level
    #             if len(node_queue) > 0:
    #                 node_queue.append(None)

    #             # prepare for the next level
    #             level_list = deque()
    #             is_order_left = not is_order_left

    #     return ret

    # # dfs: O(N) and O(H)
    # def zigzagLevelOrder(self, root):
    #     from collections import deque

    #     res = []
    #     if not root:
    #         return res

    #     def dfs(node, level):
    #         if level >= len(res):
    #             res.append(deque([node.val]))
    #         else:
    #             if level % 2 == 0:
    #                 res[level].append(node.val)
    #             else:
    #                 res[level].appendleft(node.val)
    #         for next_node in [node.left, node.right]:
    #             if next_node:
    #                 dfs(next_node, level + 1)

    #     dfs(root, 0)
    #     return res

    # dfs without recursion: O(N) and O(H)
    def zigzagLevelOrder(self, root):
        from collections import deque

        res = []
        if not root:
            return res

        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level >= len(res):
                res.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
            for next_node in [node.right, node.left]:
                if next_node:
                    stack.append((next_node, level + 1))
        return res
# @lc code=end

