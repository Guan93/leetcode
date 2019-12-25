#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def merge(self, h1, h2):
    #     dummy = tail = ListNode(None)
    #     while h1 and h2:
    #         if h1.val < h2.val:
    #             tail.next, tail, h1 = h1, h1, h1.next
    #         else:
    #             tail.next, tail, h2 = h2, h2, h2.next

    #     tail.next = h1 or h2
    #     return dummy.next

    # def sortList(self, head):
    #     if not head or not head.next:
    #         return head

    #     pre, slow, fast = None, head, head
    #     while fast and fast.next:
    #         pre, slow, fast = slow, slow.next, fast.next.next
    #     pre.next = None

    #     return self.merge(*map(self.sortList, (head, slow)))

    # merge sort, recursively
    def sortList(self, head):
        if not (head and head.next):
            return head
        # divide list into two parts
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first, second = head, slow.next
        # cut down the first part
        slow.next = None
        # merge in-place without dummy node
        first = self.sortList(first)
        second = self.sortList(second)
        return self.merge(first, second)

    def merge(self, l, r):
        if not (l and r):
            return l or r
        # get the return node "head"
        if l.val > r.val:
            l, r = r, l
        head = pre = l
        l = l.next
        while l and r:
            if l.val <= r.val:
                l = l.next
            else:
                pre.next = r
                r.next, r = l, r.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head


# @lc code=end
