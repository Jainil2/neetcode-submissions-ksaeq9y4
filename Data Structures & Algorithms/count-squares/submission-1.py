class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (px, py), cnt in list(self.points.items()):
            if px == x and py != y:
                d = py - y

                res += cnt * self.points[(x + d, y)] * self.points[(x + d, py)]

                res += cnt * self.points[(x - d, y)] * self.points[(x - d, py)]

        return res