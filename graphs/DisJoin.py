# t.c. is O(4*alpha) where alpha is near to 1 , so it is O(constant)
class Disjoin:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1) 

    def findparent(self,node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findparent(self.parent[node])

        return self.parent[node]

    def  union(self,u,v):
        pu = self.findparent(u)
        pv = self.findparent(v)
        
        if pu == pv :
            return 
        
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        elif self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else :
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
            
d = Disjoin(7)

d.union(1,2)
d.union(2,3)
d.union(4,5)
d.union(6,7)
d.union(5,6)
d.union(3,7)

print(d.findparent(1))
print(d.findparent(7))