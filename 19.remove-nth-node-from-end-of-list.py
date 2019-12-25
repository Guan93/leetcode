#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # two passes
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     curr = head
    #     N = 0
    #     while curr:
    #         curr = curr.next
    #         N += 1
    #     if n == N:
    #         return head.next

    #     i = 0
    #     curr = head
    #     while i < N - n - 1:
    #         curr = curr.next
    #         i += 1
    #     to_delete = curr.next
    #     curr.next = to_delete.next
    #     del to_delete

    #     return head

    # one pass, two pointers
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


# @lc code=end
