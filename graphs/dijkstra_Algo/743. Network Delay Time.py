from collections import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n+1)]
        
        for u,v,w in times:
            adj_list[u].append([v,w])
        
        dist = [float("inf") for _ in range(n+1)]
        dist[k] = 0
        queue = []
        heapq.heappush(queue,[0,k])
        while queue :
            distance,node = heapq.heappop(queue)
            if dist[node] < distance :
                continue
            for current_node,current_dis in adj_list[node] :
                new_dist = current_dis + distance
                if new_dist < dist[current_node] :
                    dist[current_node] = new_dist 
                    heapq.heappush(queue,[new_dist,current_node])
            
        maxi = max(dist[1:])
        if maxi == float("inf") :
            return -1
        return maxi
