#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self):
        self.cloned = dict()

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node.val in self.cloned:
            return self.cloned[node.val]

        new_node = Node(val=node)
        new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return new_node


# @lc code=end
