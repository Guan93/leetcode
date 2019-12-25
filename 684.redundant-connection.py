#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start


class UF:
    def __init__(self, n) -> None:
        self._parent = list(range(n))
        self.count = n

    def find(self, p):
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def is_connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self._parent[root_q] = root_p
            self.count -= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges) + 1)
        res = []
        for u, v in edges:
            if uf.is_connected(u, v):
                res.append([u, v])
            uf.union(u, v)
        return res[-1]


# @lc code=end
