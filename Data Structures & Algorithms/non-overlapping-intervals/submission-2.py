class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x : x[1])
        prev_end = sorted_intervals[0][1]
        ans = 0
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] >= prev_end:
                prev_end = sorted_intervals[i][1]
            else:
                ans += 1
        return ans
