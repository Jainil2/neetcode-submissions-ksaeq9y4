class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            if node in dist:
                continue
            
            dist[node] = time

            for adj, w in graph[node]:
                if adj not in dist:
                    heapq.heappush(pq, (w + time, adj))
            
        if len(dist) != n:
            return -1
        
        return max(dist.values())