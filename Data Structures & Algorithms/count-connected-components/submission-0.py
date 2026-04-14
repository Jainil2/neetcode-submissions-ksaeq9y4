class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        freq = defaultdict(list)
        for x, y in edges:
            freq[y].append(x)
            freq[x].append(y)

        visited = set()
        count = 0

        def dfs(root):
            visited.add(root)
            for adj in freq[root]:
                if adj not in visited:
                    dfs(adj)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count