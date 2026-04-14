class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        h = []
        if a > 0:
          heapq.heappush(h, (-a, "a"))
        if b > 0:
          heapq.heappush(h, (-b, "b"))
        if c > 0:
          heapq.heappush(h, (-c, "c"))
        while h:
          count, char = heapq.heappop(h)
          if len(res) >= 2 and res[-1] == res[-2] and res[-1] == char:
            if h:
              count2, char2 = heapq.heappop(h)
              res += char2
              count2 += 1
              if count2 < 0:
                heapq.heappush(h, (count2, char2))
              heapq.heappush(h, (count, char))
            else:
              break
          else:
            res += char
            count += 1
            if count < 0:
              heapq.heappush(h, (count, char))
        return res