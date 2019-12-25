import heapq
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n_workers, n_bikes = len(workers), len(bikes)
        heaps = [[] for _ in range(n_workers)]

        # denote n_workers as n and n_bikes as m
        # O(nmlogm)
        for i in range(n_workers):
            for j in range(n_bikes):
                heapq.heappush(heaps[i], (self._Manhattan(workers[i], bikes[j]), i, j))
        nearest_triples = [heapq.heappop(heaps[i]) for i in range(n_workers)]
        heapq.heapify(nearest_triples)
        ans = [-1] * n_workers
        occupied_bikes = [False] * n_bikes
        i = 0
        # O(nlogn)
        while i < n_workers:
            _, worker_idx, bike_idx = heapq.heappop(nearest_triples)
            if not occupied_bikes[bike_idx]:
                occupied_bikes[bike_idx] = True
                ans[worker_idx] = bike_idx
                i += 1
            else:
                heapq.heappush(nearest_triples, heapq.heappop(heaps[worker_idx]))
        return ans

    def _Manhattan(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
