#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head is not None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        hare, tortoise = head, head
        pt1 = head

        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                pt2 = hare
                while pt1 != pt2:
                    pt1 = pt1.next
                    pt2 = pt2.next
                return pt1
        return


# @lc code=end
