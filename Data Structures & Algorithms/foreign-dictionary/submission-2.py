class Solution:
    def topologicalsort(self, graph, indegree):
        res = ""
        q = deque()
        for key, val in indegree.items():
            if not val:
                q.append(key) 
        while q:
            node = q.popleft()
            res += node
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        return res


    def foreignDictionary(self, words: List[str]) -> str:  
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(1, len(words)):
            a = words[i - 1]
            b = words[i]
            if len(a) > len(b) and a.startswith(b):
                return ""
            for k in range(min(len(a), len(b))):
                if a[k] != b[k]:
                    if b[k] not in graph[a[k]]:
                        graph[a[k]].add(b[k])
                        indegree[b[k]] += 1
                    break
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
                if char not in indegree:
                    indegree[char] = 0
        result = self.topologicalsort(graph, indegree)
        return result if len(result) == len(indegree) else ""