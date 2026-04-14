class Solution:
    def dfs(self, node, p, graph, vis, n):
        vis[node] = True
        for adj in graph[node]:
            if adj != p and vis[adj]:
                return False
            if not vis[adj]:
                self.dfs(adj, node, graph, vis, n)
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        vis = [False] * n
        self.dfs(0, -1, graph, vis, n)
        res = True
        for v in vis:
            res = res and v
        return res