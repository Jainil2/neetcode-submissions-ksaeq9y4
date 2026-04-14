from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        vis = {}  # old node -> new node mapping
        
        def dfs(root):
            if root in vis:
                return vis[root]
            
            # Create the clone
            clone_root = Node(root.val)
            vis[root] = clone_root  # store mapping
            
            # Recursively clone neighbors
            for neighbor in root.neighbors:
                clone_root.neighbors.append(dfs(neighbor))
            
            return clone_root
        
        return dfs(node)
