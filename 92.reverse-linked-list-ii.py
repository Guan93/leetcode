#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self) -> None:
        self.successor = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseUntil(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverseUntil(self, head, n):
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseUntil(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last


# @lc code=end
