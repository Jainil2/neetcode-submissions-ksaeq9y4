class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        h = []
        for k, v in freq.items():
          heapq.heappush(h, (-v, k))
        res = ""
        prev = (0, "")
        while h:
          count, char = heapq.heappop(h)
          res += char

          if prev[0] < 0:
            heapq.heappush(h, prev)

          count += 1
          prev = (count, char)
        return res if len(res) == len(s) else ""