from collections import deque
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]

        for u,v,d in flights :
            adj_list[u].append([v,d])

        queue = deque()
        queue.append([src,0,0])

        dist = [float('inf')] * n
        dist[src] = 0

        while len(queue)!= 0 :
            node,weight,stop = queue.popleft()

            if stop > k and node != dst :
                continue
            
            for adjNode,w in adj_list[node]:
                if weight + w < dist[adjNode] : 
                    dist[adjNode] = weight + w
                    queue.append([adjNode,w+weight,stop+1])
            

        return -1 if dist[dst] == float('inf') else dist[dst]