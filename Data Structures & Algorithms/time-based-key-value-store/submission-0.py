from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arr or not self.arr[key]:
            return ""

        values = self.arr[key]
        i = bisect.bisect_right(values, (timestamp, chr(255)))

        if i == 0:
            return ""

        return values[i - 1][1]
