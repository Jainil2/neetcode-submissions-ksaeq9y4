from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        parent = {}
        found = False
        cycle_u = cycle_v = None

        def dfs(u, p):
            nonlocal found, cycle_u, cycle_v
            visited.add(u)
            for w in adj[u]:
                if found:
                    return
                if w == p:
                    continue
                if w in visited:
                    found = True
                    cycle_u = u
                    cycle_v = w
                    return
                parent[w] = u
                dfs(w, u)

        for node in adj:
            if node not in visited:
                parent[node] = -1
                dfs(node, -1)
                if found:
                    break

        cycle_nodes = set()
        if found:
            cur = cycle_u
            cycle_nodes.add(cycle_v)  
            while True:
                cycle_nodes.add(cur)
                if cur == cycle_v:
                    break
                cur = parent[cur]

        for x, y in reversed(edges):
            if x in cycle_nodes and y in cycle_nodes:
                return [x, y]

        return []  
