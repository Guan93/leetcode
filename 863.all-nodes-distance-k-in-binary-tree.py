#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143798/1ms-beat-100-simple-Java-dfs-with(without)-hashmap-including-explanation
# two pass: O(n) and O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.path = dict()
        self.res = []
        self.find_path(root, target)
        self.dfs(root, K, self.path[root.val])
        return self.res

    def find_path(self, root, target):
        if not root:
            return -1
        if root is target:
            self.path[root.val] = 0
            return 0

        for child in [root.left, root.right]:
            distance = self.find_path(child, target)
            if distance >= 0:
                self.path[root.val] = distance + 1
                return distance + 1

        return -1

    def dfs(self, root, K, distance):
        if not root:
            return
        distance = self.path.get(root.val, distance)
        if distance == K:
            self.res.append(root.val)
        self.dfs(root.left, K, distance + 1)
        self.dfs(root.right, K, distance + 1)


# rebuild a graph from the tree and then do bfs starting from the target
# O(n) and O(n)
class Solution:
    def distanceK(self, root, target, K):
        import collections

        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)

        conn = collections.defaultdict(list)
        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)
        return bfs

# @lc code=end
