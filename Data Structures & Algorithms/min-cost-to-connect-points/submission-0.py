from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        inMST = [False]*n
        minDist = [float('inf')]*n
        minDist[0] = 0
        res = 0

        for _ in range(n):
            u = -1
            curMin = float('inf')
            for i in range(n):
                if not inMST[i] and minDist[i] < curMin:
                    curMin = minDist[i]
                    u = i

            inMST[u] = True
            res += curMin

            for v in range(n):
                if not inMST[v]:
                    dist = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                    if dist < minDist[v]:
                        minDist[v] = dist
        return res