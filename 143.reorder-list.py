#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) and O(n)
class Solution1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def helper(head, tail):
            if head is tail or head.next is tail:
                return head
            new_head, new_tail = head.next, prev[tail]
            head.next = tail
            new_tail.next = None
            tail.next = helper(new_head, new_tail)
            return head

        if not head or not head.next:
            return

        prev = dict()
        tail = head
        while tail.next:
            prev[tail.next] = tail
            tail = tail.next
        helper(head, tail)


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # find median(if two, then the second one)
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        first, second = head, slow

        # reverse the second half
        second = self.reverseList(second)

        # merge two list
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

# @lc code=end
