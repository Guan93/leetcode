#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start


# top-down dp: O(kn^2) and O(kn)
# (notice that the first parameter "src" stays the same during the recursion, and keeping it here is just for ease of understanding)
class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int,
                          K: int) -> int:
        from functools import lru_cache
        from collections import defaultdict

        @lru_cache(None)
        def dp(src, dst, k):
            if src == dst:
                return 0
            if k == 0:
                res = direct_costs[dst].get(src)
                return res if res is not None else float("inf")
            res = float("inf")
            for stop in direct_costs[dst]:
                res = min(res, dp(src, stop, k - 1) + direct_costs[dst][stop])
            return res

        direct_costs = defaultdict(dict)
        for from_, to, cost in flights:
            direct_costs[to][from_] = cost
        ans = dp(src, dst, K)
        return ans if ans < float("inf") else -1


# bottom-up dp, same idea: O(kn^2) and O(n)
# this is actually bellman ford
class Solution2:
    def findCheapestPrice(self, n, flights, src, dst, K):
        INF = float('inf')
        mn = [INF] * n
        mn[src] = 0
        # mn[i] maintains the costs from src to i within k stops

        for k in range(K + 1):
            newmn = mn[:]
            for (a, b, cost) in flights:
                newmn[b] = min(newmn[b], mn[a] + cost)
            mn = newmn

        return mn[dst] if mn[dst] != INF else -1


# @lc code=end
