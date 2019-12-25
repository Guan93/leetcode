#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
import collections


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
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        uf = UF(20000)
        for x, y in stones:
            uf.union(x, y + 10000)
        return len(stones) - len({uf.find(x) for x, _ in stones})


# @lc code=end
