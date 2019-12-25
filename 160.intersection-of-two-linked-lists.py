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
    # O(N) and O(1) without knowing lengths
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
    #     lenA = lenB = 0
    #     currA, currB = headA, headB
    #     while currA:
    #         currA = currA.next
    #         lenA += 1
    #     while currB:
    #         currB = currB.next
    #         lenB += 1
    #     # make sure A is longer
    #     if lenA > lenB:
    #         curr_long, curr_short = headA, headB
    #         skip = lenA - lenB
    #     else:
    #         curr_long, curr_short = headB, headA
    #         skip = lenB - lenA
    #     for i in range(skip):
    #         curr_long = curr_long.next
    #     while curr_long != curr_short:
    #         curr_long = curr_long.next
    #         curr_short = curr_short.next
    #     return curr_long

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
