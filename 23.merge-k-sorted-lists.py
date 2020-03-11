#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# brute force: put all numbers in a array and sort it: O(nlogn) and O(n)


# improve by priority queue: O(nlogk) and O(k)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        heads = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heads, (lists[i].val, i))

        dummy = ListNode(0)
        head = dummy
        while heads:
            _, i = heapq.heappop(heads)
            head.next = lists[i]
            head = head.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heads, (lists[i].val, i))

        return dummy.next


# # O(kn) and O(1)
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         def _min_index(lists: List[ListNode]):
#             min_idx = -1
#             min_val = float("inf")
#             for i, l in enumerate(lists):
#                 if l and min_val > l.val:
#                     min_idx = i
#                     min_val = l.val
#             return min_idx

#         dummy = ListNode(0)
#         first = dummy
#         while True:
#             min_idx = _min_index(lists)
#             if min_idx == -1:
#                 break
#             first.next = lists[min_idx]
#             lists[min_idx] = lists[min_idx].next
#             first = first.next
#         return dummy.next


# # divide and conquer: O(nlogk)(every node is visited logk times) and O(log(k))
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         first = dummy
#         while l1 and l2:
#             if l1.val < l2.val:
#                 first.next = l1
#                 l1 = l1.next
#             else:
#                 first.next = l2
#                 l2 = l2.next
#             first = first.next
#         first.next = l1 if l1 else l2
#         return dummy.next

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         if len(lists) == 1:
#             return lists[0]
#         else:
#             mid = (len(lists) + 1) // 2
#             return self.mergeTwoLists(
#                 self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))


# @lc code=end
