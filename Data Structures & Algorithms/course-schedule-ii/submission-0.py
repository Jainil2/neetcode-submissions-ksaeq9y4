class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    def create(self, edges):
        for u, v in edges:
            self.graph[v].append(u)
        return 
    def topological_sort_utils(self, start, vis, st):
        vis[start] = 1
        for adj in self.graph[start]:
            if vis[adj] == 0:
                if not self.topological_sort_utils(adj, vis, st):
                    return False
            elif vis[adj] == 1:
                return False
        vis[start] = 2
        st.append(start)
        return True
    def topological_sort(self, n):
        vis = [0] * n
        st = []
        for i in range(n):
            if vis[i] == 0:
                if not self.topological_sort_utils(i, vis, st):
                    return []
        return st[::-1]

    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.create(pre)
        return self.topological_sort(numCourses)
        