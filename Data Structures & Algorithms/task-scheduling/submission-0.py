class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        h = []
        for x, y in freq.items():
            heapq.heappush(h, - y)
        q = deque()
        t = 0
        while q or h:
            while q and q[0][0] == t:
                _, y = q.popleft()
                heapq.heappush(h, y)

            if h:
                ele = heapq.heappop(h)
                if ele + 1 < 0:
                    q.append((t + n + 1, ele + 1))
            t += 1
        return t
                        
                    