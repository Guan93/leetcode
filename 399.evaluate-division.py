#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        eq_dict = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            eq_dict[a][b] = val
            eq_dict[b][a] = 1 / val
        for (a, b), val in zip(equations, values):
            for c in eq_dict[a]:
                eq_dict[b][c] = eq_dict[a][c] / eq_dict[a][b]
                eq_dict[c][b] = 1 / eq_dict[b][c]
            for c in eq_dict[b]:
                eq_dict[a][c] = eq_dict[b][c] / eq_dict[b][a]
                eq_dict[c][a] = 1 / eq_dict[a][c]

        res = []
        for a, b in queries:
            curr_res = -1
            for c in eq_dict:
                if a in eq_dict and b in eq_dict[a]:
                    curr_res = eq_dict[a][b]
                    break
            res.append(curr_res)
        return res


# directed graph: Building graph: O(E) and O(E), each query: O(N) and O(1)
class Solution(object):
    def calcEquation(self, equations, values, queries):

        graph = {}

        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]

            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)

        def find_path(query):
            b, e = query

            if b not in graph or e not in graph:
                return -1.0

            q = collections.deque([(b, 1.0)])
            visited = set()

            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))

            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]
# @lc code=end

