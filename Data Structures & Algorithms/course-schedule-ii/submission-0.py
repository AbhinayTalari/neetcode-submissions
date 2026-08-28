from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        order = []
        visited, path = set(), set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
            path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order