from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):    
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for val in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][val] != float("inf") and dist[val][j] != float("inf") :
                        dist[i][j] = min(dist[i][j],dist[i][val]+dist[val][j]) 

        city = -1 
        neighbours = n

        for i in range(n):
            count = 0
            for j in range(n) :
                if dist[i][j] <= distanceThreshold :
                    count +=1 

            if count <= neighbours :
                neighbours = count 
                city = i

        return city 