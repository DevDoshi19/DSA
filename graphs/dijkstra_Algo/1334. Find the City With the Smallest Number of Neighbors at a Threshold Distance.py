from typing import List
import heapq
import sys
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj_list = [[] for _ in range(n)]
        for u,v,w in edges:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w])

        
        city = -1
        neighbours = n 

        for i in range(n):
            dist = [sys.maxsize for _ in range(n)]
            dist[i] = 0
            count = 0  
            queue = [[0,i]]
            while len(queue):
                dst , node = heapq.heappop(queue)
                if dst > dist[node]:
                    continue
                for adjNode ,weight in adj_list[node]:
                    new_weight = weight + dst 
                    if new_weight <= dist[adjNode] : 
                        dist[adjNode] = new_weight
                        heapq.heappush(queue,[new_weight,adjNode])
                        
            for d in dist:
                if d <= distanceThreshold:
                    count +=1 

            if count <= neighbours:
                neighbours = count
                city = i

        return city