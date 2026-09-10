class Solution:
    def bellmanFord(self, V, edges, src):
            
        dist = [10**8 for _ in range(V)]
        dist[src] = 0 
        
        # try to n-1 times relax all the edges
        # bellmonford is used to find the shortest path in a graph with negative weights
        for _ in range(1,V):
            for edge in edges :
                u, v, weight = edge[0], edge[1], edge[2]
                if dist[u] != 10**8 and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                
        # 1 more time to check if there is a negative cycle
        # if we can relax any edge then there is a negative cycle
        for edge in edges:
            u, v, weight = edge[0], edge[1], edge[2]
            if dist[u] != 10**8 and dist[u] + weight < dist[v]:
                return [-1]
            
        return dist