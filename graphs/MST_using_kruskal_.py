class Disjointset:
    def __init__(self, n):
        # Initialize parent to point to itself and ranks to 0
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def findparent(self, u):
        # Corrected array lookup and implemented path compression
        if self.parent[u] != u:
            self.parent[u] = self.findparent(self.parent[u])
        return self.parent[u]
        
    def union(self, u, v):
        pu = self.findparent(u)
        pv = self.findparent(v)
        
        if pu == pv:
            return False
            
        # Union by rank
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def spanningTree(self, V, edges):
        # Format incoming edges into (weight, u, v)
        # Avoids shadowing the 'edges' variable incorrectly
        formatted_edges = []
        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            formatted_edges.append((w, u, v))
            
        # Sort edges by weight for Kruskal's algorithm
        formatted_edges.sort()
        
        dsu = Disjointset(V)
        mst_weight = 0
        edges_count = 0
        
        for w, u, v in formatted_edges:
            if dsu.union(u, v):
                mst_weight += w
                edges_count += 1
                # Optimization: Stop early if we have connected V-1 edges
                if edges_count == V - 1:
                    break
                    
        return mst_weight
