class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
            
        dist = [10**8 for _ in range(V)]
        
        dist[src] = 0 
        
        for _ in range(1,V):
            for edge in edges :
                u, v, weight = edge[0], edge[1], edge[2]
                if dist[u] != 10**8 and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                
        for edge in edges:
            u, v, weight = edge[0], edge[1], edge[2]
            if dist[u] != 10**8 and dist[u] + weight < dist[v]:
                return [-1]
            
        return dist