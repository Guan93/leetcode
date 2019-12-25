#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        dummy = Node(0, None, None, None)
        stack = [head]
        while stack:
            curr = stack.pop()
            if curr.next:
                stack.append(curr.next)
                curr.next = None
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            dummy.next = curr
            curr.prev = dummy
            dummy = curr
        head.prev = None
        return head


# @lc code=end
