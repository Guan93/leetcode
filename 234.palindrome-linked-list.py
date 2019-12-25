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
        # find the mid node and meanwhile reverse the first part
        slow = fast = head
        rev = ListNode(0)
        while fast and fast.next:
            fast = fast.next.next
            curr = slow
            slow = slow.next
            curr.next = rev.next
            rev.next = curr
        rev = rev.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# @lc code=end
