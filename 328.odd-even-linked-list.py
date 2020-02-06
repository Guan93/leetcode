#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head, even_head = ListNode(None), ListNode(None)
        odd_ptr, even_ptr = odd_head, even_head
        is_odd = True
        while head:
            if is_odd:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next
            head = head.next
            is_odd = not is_odd

        odd_ptr.next = even_head.next
        even_ptr.next = None
        head = odd_head.next
        return head


# @lc code=end
