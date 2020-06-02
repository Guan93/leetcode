#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        if not n:
            return 0

        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]:
                    uf.connect(i, j)

        return uf.count


class UF:
    def __init__(self, n) -> None:
        self.root = list(range(n))
        self.count = n

    def find_root(self, p):
        while p != self.root[p]:
            p = self.root[p]
        return p

    def is_connected(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        return root_p == root_q

    def connect(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        if root_p != root_q:
            self.root[root_q] = root_p
            self.count -= 1


class Solution2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = True

            for j in range(n):
                if not visited[j] and M[i][j]:
                    dfs(j)

        n = len(M)
        if not n:
            return 0

        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count

# @lc code=end

