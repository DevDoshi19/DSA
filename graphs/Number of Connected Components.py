class Disjoin :
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * n 
        
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv :
            return False
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else :
            self.parent[pu] = pv
            self.rank[pu] += 1
            
        return True 
    
class Solution:
    def countConnected(self, V, edges):
        # code here 
        count = V
        d = Disjoin(V)
        for u,v in edges:
            if d.union(u,v) :
                count -=1 
            
        return count
            