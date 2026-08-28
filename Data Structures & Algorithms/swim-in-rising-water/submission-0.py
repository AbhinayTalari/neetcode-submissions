from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)] # time, r, c

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return t
            if visit[r][c]:
                continue
            visit[r][c] = True

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1