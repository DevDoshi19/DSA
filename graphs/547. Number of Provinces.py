from typing import List
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
            return 
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else :
            self.parent[pu] = pv
            self.rank[pu] += 1
             
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        d = Disjoin(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])) :
                if isConnected[i][j] == 1 and i != j :
                    d.union(i,j)
            
        for i in range(len(isConnected)):
            if d.find(i) == i :
                count +=1
        
        return count
            