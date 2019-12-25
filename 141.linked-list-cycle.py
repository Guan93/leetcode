#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head is not None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

    # Floyd's Tortoise and Hare
    def hasCycle(self, head: ListNode) -> bool:
        """
        A tortoise and a hare running with different speed.
        If there is a circle:
            in a base case, the tortoise is one step ahead the hare,
            then in the next turn they will meet;
            all other cases will reduce to the base case.
        """
        if head is None or head.next is None:
            return False
        hare, tortoise = head.next, head
        while hare != tortoise:
            if hare is None or hare.next is None:
                return False
            hare = hare.next.next
            tortoise = tortoise.next
        return True


# @lc code=end
