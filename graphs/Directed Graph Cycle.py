#  https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    
    def dfs(self,current_node,visited,path,adj_list):
        visited[current_node] = 1
        path[current_node] = 1
        for adjNode in adj_list[current_node] :
            if visited[adjNode] == 1 and path[adjNode] == 0:
                continue
            elif visited[adjNode] == 1 and path[adjNode] == 1:
                return True
            
            if self.dfs(adjNode,visited,path,adj_list):
                return True
            
        path[current_node] = 0
        
        return False
            
    
    def isCyclic(self, V, edges):
        # code here
        visited = [0 for _ in range(V)]
        path = [0 for _ in range(V)]
        
        adj_list = [[] for _ in range(V)]
        
        for u,v in edges :
            adj_list[u].append(v)
            
        for i in range(0,len(visited)):
            
            if visited[i] == 0:
                if self.dfs(i,visited,path,adj_list) :
                    return True
                    
        return False 


# we can also do this using single visited variable , if we use 0 for unvisited , 1 for visited and 2 for path visited then we can do this in single visited variable.

class Solution1:
    
    def dfs(self,current_node,visited,adj_list):
        visited[current_node] = 2
        
        for adjNode in adj_list[current_node] :
            if visited[adjNode] == 1 :
                continue
            elif visited[adjNode] == 2:
                return True
            
            if self.dfs(adjNode,visited,adj_list):
                return True
            
        visited[current_node] = 1
        
        return False
            
    
    def isCyclic(self, V, edges):
        # code here
        visited = [0 for _ in range(V)]
        
        adj_list = [[] for _ in range(V)]
        
        for u,v in edges :
            adj_list[u].append(v)
            
        for i in range(0,len(visited)):
            
            if visited[i] == 0:
                if self.dfs(i,visited,adj_list) :
                    return True
                    
        return False 
    
# s.c. becomes O(n) from O(2n) 
# t.c. = O(V+E)