#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc code=start
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.nei = set()


class Solution:
    # dfs: O(n) and O(n)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [Node(i) for i in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].nei.add(graph[course])

        post = []
        marked = [False] * numCourses
        on_stack = [False] * numCourses
        self.has_cycle = False

        def dfs(node):
            marked[node.val] = True
            on_stack[node.val] = True

            for nei in node.nei:
                if self.has_cycle:
                    return
                if not marked[nei.val]:
                    dfs(nei)
                elif on_stack[nei.val]:
                    self.has_cycle = True
                    return
            on_stack[node.val] = False
            post.append(node.val)

        for node in graph:
            if not marked[node.val]:
                dfs(node)

        return post[::-1] if not self.has_cycle else []


# @lc code=end
