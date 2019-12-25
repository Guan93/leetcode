#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start

# # dfs: O(N + E) and O(N)
# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         N = len(graph)
#         self._visited = [False] * N
#         self._onstack = set()
#         self._oncircle = set()

#         for v in range(N):
#             if not self._visited[v]:
#                 self._dfs(graph, v)
#         return sorted(list(set(range(N)) - self._oncircle))

#     def _dfs(self, graph: List[List[int]], v: int) -> None:
#         self._visited[v] = True
#         self._onstack.add(v)
#         for w in graph[v]:
#             if w in self._oncircle:
#                 self._oncircle.update(self._onstack)
#                 continue
#             if not self._visited[w]:
#                 self._dfs(graph, w)
#             elif w in self._onstack:
#                 self._oncircle.update(self._onstack)
#         self._onstack.remove(v)


# white-gray-black dfs: O(N + E) and O(N)
import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        # white: not visited; mark a node gray on entry and black on exit
        colors = [0] * len(graph)

        def dfs(node):
            if colors[node] != WHITE:
                return colors[node] == BLACK

            colors[node] = GRAY
            for nei in graph[node]:
                if colors[nei] == BLACK:
                    continue
                if colors[nei] == GRAY or not dfs(nei):
                    return False
            colors[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))

# @lc code=end
