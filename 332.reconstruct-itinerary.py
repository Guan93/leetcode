#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#


# @lc code=start
class Solution:
    # backtracking
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict, Counter

        self.res = ["JFK"]
        graph = defaultdict(list)
        edges = Counter()

        for from_, to in tickets:
            graph[from_].append(to)
            edges[(from_, to)] += 1

        for from_ in graph:
            graph[from_].sort()

        def dfs(from_):
            if len(self.res) == len(tickets) + 1:
                return True

            for to in graph[from_]:
                if edges[(from_, to)]:
                    edges[(from_, to)] -= 1
                    self.res.append(to)
                    if dfs(to):
                        return True
                    self.res.pop()
                    edges[(from_, to)] += 1

            return False

        dfs("JFK")
        return self.res

    # Hierholzer's Algorithm (can be viewed as post order dfs in this problem)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict

        def dfs(from_):
            while graph[from_]:
                to = graph[from_].pop()
                dfs(to)
            res.append(from_)

        graph = defaultdict(list)
        for from_, to in tickets:
            graph[from_].append(to)

        for from_ in graph:
            graph[from_].sort(reverse=True)

        res = []
        dfs("JFK")
        return res[::-1]

# @lc code=end
