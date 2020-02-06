#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    # # bfs: O(n) and O(n)
    # def connect(self, root: 'Node') -> 'Node':
    #     from collections import deque

    #     if not root:
    #         return root
    #     queue = deque([root])
    #     while queue:
    #         size = len(queue)
    #         for i in range(size):
    #             node = queue.popleft()
    #             for child in [node.left, node.right]:
    #                 if child:
    #                     queue.append(child)
    #             if i < size - 1:
    #                 node.next = queue[0]
    #     return root

    # connect all nodes in level N when we are at level N - 1
    # O(n) and O(1)
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
# @lc code=end

