from typing import List
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for u,v,d in roads:
            adj_list[u].append([v,d])
            adj_list[v].append([u,d])

        dist = [float("inf") for _ in range(n)]
        num_of_ways = [0 for _ in range(n)]

        dist[0]= 0
        num_of_ways[0] = 1

        queue = [[0,0]]

        while len(queue) != 0 :
            dst, node = heapq.heappop(queue) 

            if dst > dist[node]:
                continue

            for adjNode,weight in adj_list[node] :
                new_d = dst + weight 

                if new_d < dist[adjNode] :
                    dist[adjNode] = new_d
                    num_of_ways[adjNode] = num_of_ways[node]
                    heapq.heappush(queue,[new_d,adjNode])

                elif new_d == dist[adjNode] :
                    num_of_ways[adjNode] += num_of_ways[node]

        return num_of_ways[n-1] % (10**9 + 7)