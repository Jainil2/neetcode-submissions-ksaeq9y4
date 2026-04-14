class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        visited = [0] * numCourses 
        def dfs(node):
            if visited[node] == 1: 
                return True
            if visited[node] == 2:  
                return False

            visited[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            visited[node] = 2  
            return False

        for i in range(numCourses):
            if dfs(i):
                return False 

        return True  
