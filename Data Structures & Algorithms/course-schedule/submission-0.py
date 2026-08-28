from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indeg[crs] += 1

        q = deque([i for i in range(numCourses) if indeg[i]==0])
        visited = 0

        while q:
            u = q.popleft()
            visited += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v]==0:
                    q.append(v)

        return visited == numCourses