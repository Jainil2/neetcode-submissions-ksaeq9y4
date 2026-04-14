class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
      pending = [] 
      available = [] 
      for i, (enqueue, processTime) in enumerate(tasks):
        heapq.heappush(pending, (enqueue, processTime, i))

      time  = 0
      res = []

      while pending or available:
          while pending and pending[0][0] <= time:
              _, processTime, i = heapq.heappop(pending)
              heapq.heappush(available, (processTime, i))
              
          if not available:
              time = pending[0][0]
              continue
          
          processTime, i = heapq.heappop(available)
          time = time + processTime
          res.append(i)

      return res