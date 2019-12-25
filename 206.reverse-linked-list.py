#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iterative O(n), O(1)
    # def reverseList(self, head: ListNode) -> ListNode:
    #     dummy = ListNode(0)
    #     while head:
    #         curr = head
    #         head = head.next
    #         curr.next = dummy.next
    #         dummy.next = curr
    #     return dummy.next
    
    # recursive O(n), O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
# @lc code=end
