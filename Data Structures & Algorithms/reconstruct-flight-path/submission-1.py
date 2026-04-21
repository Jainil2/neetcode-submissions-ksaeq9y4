class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()
        for u, v in tickets:
            graph[u].append(v)

        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph:
                return False
            
            temp = list(graph[src])
            for i, v in enumerate(temp):
                graph[src].pop(i)
                res.append(v)
                if dfs(v): return True
                graph[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res