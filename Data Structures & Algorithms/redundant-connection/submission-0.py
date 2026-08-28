from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges)+1))
        rank = [1]*(len(edges)+1)

        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]

        def union(a,b):
            pa,pb = find(a), find(b)
            if pa==pb:
                return False
            if rank[pa] < rank[pb]:
                pa,pb = pb,pa
            par[pb]=pa
            rank[pa]+=rank[pb]
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []