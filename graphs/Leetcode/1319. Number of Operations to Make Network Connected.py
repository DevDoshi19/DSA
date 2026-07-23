from collections import deque
from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
       
        if len(connections) < n - 1:
            return -1
        
        adj_list = [[] for _ in range(n)]
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u) 
            
        visited = [False] * n
        components = 0
  
        for i in range(n):
            if not visited[i]:
                components += 1
                
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    node = queue.popleft()
                    for neighbor in adj_list[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            
        return components - 1
