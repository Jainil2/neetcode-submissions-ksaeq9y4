class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        for i, (n, f, t) in enumerate(trips):
          heapq.heappush(h, (f, t, n))
        start, cap = 0, capacity
        temp = []
        while h:
          while temp and temp[0][0] <= start:
            cap += temp[0][2]
            heapq.heappop(temp) 
          f, t, n = heapq.heappop(h)
          if n > cap:
            return False
          heapq.heappush(temp, (t, f, n))
          if h:
            start = h[0][0]
          else:
            break
          cap -= n
        return True
