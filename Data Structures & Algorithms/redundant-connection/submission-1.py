class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                par[px] = py
            elif rank[px] > rank[py]:
                par[py] = px
            else:
                par[py] = px
                rank[px] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
