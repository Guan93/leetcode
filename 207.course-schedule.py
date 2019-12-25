#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

# # detect circle
# class DiGraph:
#     def __init__(self, V: int) -> None:
#         self.V = V
#         self.E = 0
#         self.adj = [[] for _ in range(V)]

#     def add_edge(self, v: int, w: int) -> None:
#         self.adj[v].append(w)

# class DiCycle:
#     def __init__(self, G: DiGraph) -> None:
#         self._visited = [False] * G.V
#         self._onstack = [False] * G.V
#         self.has_cycle = False

#         for v in range(G.V):
#             if not self._visited[v]:
#                 self._dfs(G, v)

#     def _dfs(self, G: DiGraph, v: int):
#         self._visited[v] = True
#         self._onstack[v] = True
#         for w in G.adj[v]:
#             if self.has_cycle:
#                 return
#             if not self._visited[w]:
#                 self._dfs(G, w)
#             elif self._onstack[w]:
#                 self.has_cycle = True
#                 return
#         self._onstack[v] = False

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         G = DiGraph(numCourses)
#         for course, pre in prerequisites:
#             G.add_edge(pre, course)
#         C = DiCycle(G)
#         return not C.has_cycle


# removing nodes with degree of zero. if nothing remains, there is no cycle
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1

        q = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            curr = q.pop(0)
            numCourses -= 1
            for w in adj[curr]:
                in_degree[w] -= 1
                if in_degree[w] == 0:
                    q.append(w)

        return numCourses == 0


# @lc code=end
