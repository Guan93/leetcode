#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start

import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graphs = collections.defaultdict(list)
        for u, v, w in times:
            graphs[u].append((v, w))
        pq = [(0, K)]
        dist = dict()

        while pq:
            w, u = heapq.heappop(pq)
            if u in dist:
                continue
            dist[u] = w
            for v, w2 in graphs[u]:
                if v not in dist:
                    heapq.heappush(pq, (w2 + w, v))
        
        return max(dist.values()) if len(dist) == N else -1



# @lc code=end
