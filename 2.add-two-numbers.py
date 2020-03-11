#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        p1, p2, p3 = l1, l2, res

        quo = 0
        while p1 and p2:
            quo, rem = divmod(p1.val + p2.val + quo, 10)
            p3.next = ListNode(rem)
            p1, p2, p3 = p1.next, p2.next, p3.next

        p = p1 if p1 else p2
        while p:
            quo, rem = divmod(p.val + quo, 10)
            p3.next = ListNode(rem)
            p3, p = p3.next, p.next

        if quo:
            p3.next = ListNode(quo)

        return res.next

    # a more concise one
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        carry = 0
        n = res

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = ListNode(val)
            n = n.next

        return res.next

# @lc code=end

