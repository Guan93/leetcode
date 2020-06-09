#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# iteration: O(n) and O(1)
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        prev, curr, nxt = dummy, head, head.next
        while True:
            prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr
            if not curr.next or not curr.next.next:
                break
            prev, curr, nxt = curr, curr.next, curr.next.next

        return dummy.next


# recursion: O(n) and O(n)
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


# @lc code=end
