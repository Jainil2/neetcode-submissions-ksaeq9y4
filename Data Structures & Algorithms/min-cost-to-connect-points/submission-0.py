class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False 

        if rootx != rooty:
            if self.ranks[rootx] > self.ranks[rooty]:
                self.parents[rooty] = rootx
            elif self.ranks[rootx] < self.ranks[rooty]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                self.ranks[rootx] += 1
            return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    edges.append([i, j, w])
        edges.sort(key = lambda x: x[2])
        res = 0
        uf = UnionFind(n)
        for u, v, w in edges:
            if uf.union(u, v):
                res += w
        return res
