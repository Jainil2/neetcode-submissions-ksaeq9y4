class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int: 
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x.start)
        h = []
        for inte in intervals:
            if h and inte.start >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, inte.end)
        return len(h)