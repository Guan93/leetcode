#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Iterative O(N + M) and O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        first = dummy
        while l1 and l2:
            if l1.val < l2.val:
                first.next = l1
                l1 = l1.next
            else:
                first.next = l2
                l2 = l2.next
            first = first.next
        first.next = l1 if l1 else l2

        return dummy.next

    # Recursive: O(N + M) and O(N + M) 
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if not l1:
    #         return l2
    #     elif not l2:
    #         return l1
    #     elif l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l2.next, l1)
    #         return l2



# @lc code=end
