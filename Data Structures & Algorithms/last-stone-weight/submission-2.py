class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            one = -heapq.heappop(max_heap)
            two = -heapq.heappop(max_heap)
            if one == two:
                continue
            else:
                heapq.heappush(max_heap, -(one - two))
        if len(max_heap) == 0:
            return 0
        return abs(max_heap[0])