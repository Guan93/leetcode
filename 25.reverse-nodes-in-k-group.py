#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        p = head
        while p:
            p, n = p.next, n + 1

        dummy = ListNode()
        next_head = head
        prev_tail = dummy
        while n >= k:
            prev_head = next_head
            new_head, next_head = self.reverseKList(next_head, k)
            prev_tail.next = new_head
            prev_tail = prev_head
            n -= k

        if n:
            prev_tail.next = next_head

        return dummy.next

    def reverseKList(self, head: ListNode, k: int):
        dummy = ListNode(0)
        while k:
            curr = head
            head = head.next
            curr.next = dummy.next
            dummy.next = curr
            k -= 1
        return dummy.next, head


# @lc code=end
