from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1]*n

        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x

        def union(a,b):
            pa,pb = find(a), find(b)
            if pa==pb: return 0
            if rank[pa] < rank[pb]:
                pa,pb = pb,pa
            par[pb]=pa
            rank[pa]+=rank[pb]
            return 1

        res = n
        for u,v in edges:
            res -= union(u,v)
        return res