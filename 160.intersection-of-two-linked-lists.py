#
# @lc app=leetcode id=160 lang=python
#
# [160] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # O(N) and O(1) without knowing lengths: essentially the same as finding the length first
    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):
            return None
        currA, currB = headA, headB
        while currA is not currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA

    # # O(N) and O(1)
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     lenA, lenB = self.get_length(headA), self.get_length(headB)
    #     if lenA < lenB:
    #         lenA, lenB, headA, headB = lenB, lenA, headB, headA

    #     diff = lenA - lenB
    #     while diff:
    #         diff, headA = diff - 1, headA.next

    #     while headA and headB:
    #         if headA == headB:
    #             return headA
    #         headA, headB = headA.next, headB.next

    #     return None

    # def get_length(self, head):
    #     count = 0
    #     while head:
    #         count, head = count + 1, head.next
    #     return count

    # stack: O(N) and O(N)
    # def getIntersectionNode(self, headA, headB):
    #     if not (headA and headB):
    #         return None
    #     dummyA, dummyB = ListNode(0), ListNode(1)
    #     dummyA.next = headA
    #     dummyB.next = headB

    #     stackA, stackB = [], []
    #     while dummyA:
    #         stackA.append(dummyA)
    #         dummyA = dummyA.next
    #     while dummyB:
    #         stackB.append(dummyB)
    #         dummyB = dummyB.next

    #     currA, currB = stackA[-1], stackB[-1]
    #     while len(stackA) > 0 and len(stackB) > 0 and currA == currB:
    #         currA, currB = stackA.pop(), stackB.pop()
    #     return currA.next


# @lc code=end
