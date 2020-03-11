#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/No-TarjanDFS-detailed-explanation-O(orEor)-solution-(I-like-this-question)
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        def dfs(i, depth):
            if depths[i] >= 0:
                return depths[i]

            depths[i] = depth
            min_depth = n
            for nei in graph[i]:
                if depths[nei] == depth - 1:
                    continue
                nei_min_depth = dfs(nei, depth + 1)
                if nei_min_depth <= depth:
                    edges.remove(tuple(sorted([i, nei])))
                min_depth = min(min_depth, nei_min_depth)
            return min_depth

        graph = defaultdict(list)
        edges = set()
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
            edges.add(tuple(sorted([v1, v2])))
        depths = [-2] * n

        # since all nodes are connected, we don't need to loop through all nodes
        dfs(0, 0)

        return list(edges)

# @lc code=end

