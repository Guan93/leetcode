#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_length(l):
            length = 0
            while l:
                l, length = l.next, length + 1
            return length

        def addTwoNumbers(l1, l2, digit):
            if digit == 0:
                return 0, None
            f1, rest1 = l1.val, l1.next
            if digit > len2:
                f2, rest2 = 0, l2
            else:
                f2, rest2 = l2.val, l2.next
            carry, rest = addTwoNumbers(rest1, rest2, digit - 1)
            carry, f = divmod(f1 + f2 + carry, 10)
            res = ListNode(val=f, next=rest)

            return carry, res

        len1, len2 = get_length(l1), get_length(l2)
        if len1 < len2:
            len1, len2 = len2, len1
            l1, l2 = l2, l1

        carry, l = addTwoNumbers(l1, l2, len1)
        if carry:
            l = ListNode(val=carry, next=l)

        return l



# @lc code=end
