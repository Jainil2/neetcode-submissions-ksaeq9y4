class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        freq = defaultdict(list)
        for x, y in edges:
            freq[x].append(y)
            freq[y].append(x)

        visited = set()

        def dfs(root, par):
            visited.add(root)
            for adj in freq[root]:
                if adj == par:
                    continue
                if adj in visited or not dfs(adj, root):
                    return False
            return True 

        if not dfs(0, -1):
            return False
        
        return len(visited) == n