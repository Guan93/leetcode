# priority queue
import heapq
from typing import List, Set

# # brute force and pruning: TLE
# class Solution:
#     _min_sum = float("inf")

#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
#         n_workers, n_bikes = len(workers), len(bikes)

#         def _manhattan(p1: List[int], p2: List[int]) -> int:
#             return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#         visited = [False for i in range(n_bikes)]
#         distances = [[-1] * len(bikes) for _ in range(n_workers)]
#         for i in range(n_workers):
#             for j in range(n_bikes):
#                 distances[i][j] = _manhattan(workers[i], bikes[j])
#         self._helper(n_workers - 1, distances, visited, 0)
#         return self._min_sum

#     def _helper(self, worker: int, distances: List[List[int]], visited: List[bool],
#                 cur_sum: int) -> None:
#         if worker < 0:
#             self._min_sum = min(self._min_sum, cur_sum)
#             return
#         if cur_sum >= self._min_sum:
#             return
#         for bike in range(len(visited)):
#             if visited[bike]:
#                 continue
#             visited[bike] = True
#             self._helper(worker - 1, distances, visited,
#                          cur_sum + distances[worker][bike])
#             visited[bike] = False

# # dp
# class Solution:
#     def __init__(self):
#         self._map = dict()

#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
#         visited = [False] * len(bikes)
#         return self._dfs(workers, bikes, visited, 0)

#     def _dfs(self, workers: List[List[int]], bikes: List[List[int]], visited: List[bool],
#              worker_idx: int) -> int:
#         if worker_idx == len(workers):
#             return 0
#         # every visited bool array corresponds to a state. we generate a key for such
#         # state and compute and store the minimum value for all unvisited bikes in this
#         # state
#         key = self._gen_key(visited)
#         if key in self._map:
#             return self._map[key]
#         _min = float("inf")
#         for bike_idx in range(len(bikes)):
#             if visited[bike_idx]:
#                 continue
#             visited[bike_idx] = True
#             _min = min(
#                 _min,
#                 self._manhattan(workers[worker_idx], bikes[bike_idx]) + self._dfs(
#                     workers, bikes, visited, worker_idx + 1))
#             visited[bike_idx] = False
#         self._map[key] = _min
#         return _min

#     def _gen_key(self, visited: List[bool]) -> int:
#         """
#         num | (1<<k): set num's k-th bit as 1
#         num & (1<<k): get num's k-th bit
#         """
#         key = 0
#         for i in range(len(visited)):
#             if not visited[i]:
#                 key |= 1 << i
#         return key

#     def _manhattan(self, p1: List[int], p2: List[int]) -> int:
#         return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# # simplified version of the above
# class Solution:
#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
#         # dp should hold 2^(len(bikes)) elements
#         return self._dfs(workers, bikes, 0, 0, [0] * (1 << len(bikes)))

#     def _dfs(self, workers, bikes, used, worker_idx, dp) -> int:
#         def dist(p1, p2):
#             return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#         if worker_idx == len(workers):
#             return 0
#         if dp[used] > 0:
#             return dp[used]
#         _min = float("inf")
#         for bike_idx in range(len(bikes)):
#             if (used & (1 << bike_idx)) == 0:  # if unvisited
#                 used |= (1 << bike_idx)  # set ith bit
#                 _min = min(
#                     _min,
#                     dist(workers[worker_idx], bikes[bike_idx]) + self._dfs(
#                         workers, bikes, used, worker_idx + 1, dp))
#                 used &= ~(1 << bike_idx)  # unset ith bit
#         dp[used] = _min
#         return _min




class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if taken in seen: continue
            seen.add(taken)
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])
