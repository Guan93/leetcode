#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self) -> None:
        self._visited = dict()

    # Iterative, O(N) and O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        node_new = Node(head.val, None, None)
        node_old = head
        self._visited[node_old] = node_new

        while node_old:
            node_new.next = self._get_node_clone(node_old.next)
            node_new.random = self._get_node_clone(node_old.random)

            node_new = node_new.next
            node_old = node_old.next

        return self._visited[head]

    def _get_node_clone(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        if node not in self._visited:
            self._visited[node] = Node(node.val, None, None)
        return self._visited[node]

    # Iterative, O(N) and O(N)
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     if head is None:
    #         return None

    #     if head in self._visited:
    #         return self._visited[head]

    #     node = Node(head.val, None, None)
    #     self._visited[head] = node

    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)

    #     return node


# @lc code=end
