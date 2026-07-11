from typing import List

class Solution:

    def dfs(self,current_node,stack,visited,adj_list):
        
        visited[current_node] =1
        
        for adjNode,dis in adj_list[current_node]:
            if visited[adjNode] == 0 :
                self.dfs(adjNode,stack,visited,adj_list)
                
        stack.append(current_node)
        
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(V)]
        
        for u,v,d in edges:
            adj_list[u].append([v,d])
            
        visited = [0 for _ in range(V)]
        
        stack = []
        
        for i in range(len(visited)):
            if visited[i] == 0 :
                self.dfs(i,stack,visited,adj_list)
                
        distance = [float("inf") for _ in range(V)]
        distance[0] = 0 
        
        while len(stack) :
            node = stack.pop()
            dist = distance[node] # so the last node in the stack is the node with the minimum distance from the source node. So we will update the distance of all the adjacent nodes of this node., here it will be the distance of the source node which is 0. So we will update the distance of all the adjacent nodes of the source node.
            for adjNode,d in adj_list[node]:
                new_d = dist + d 
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d
                
        for i in range(len(distance)) :
            if distance[i] == float("inf"):
                distance[i] = -1
                
        return distance 
    
# here the source node is 0 and we are finding the shortest path from source node to all other nodes in the graph.