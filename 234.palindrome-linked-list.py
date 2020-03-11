#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) and O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        # find the middle point
        lower_mid = self.get_lower_mid(head)
        p1 = head
        # reverse the second half
        p2 = self.reverse_link_list(lower_mid.next)

        # check whether it's a parlindrome
        res = True
        while res and p2:
            if p1.val == p2.val:
                p1, p2 = p1.next, p2.next
            else:
                res = False

        # reverse the second half back for good programming practice
        lower_mid.next = self.reverse_link_list(lower_mid.next)

        return res

    def get_lower_mid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_link_list(self, head):
        if not head or not head.next:
            return head

        rev_head = self.reverse_link_list(head.next)
        head.next.next = head
        head.next = None
        return rev_head

# @lc code=end
