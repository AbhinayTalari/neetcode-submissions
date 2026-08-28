from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {}
        heap = [(0, k)] # time, node

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, w in adj[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        if len(dist)!= n:
            return -1
        return max(dist.values())