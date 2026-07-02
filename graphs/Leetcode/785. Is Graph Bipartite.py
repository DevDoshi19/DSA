from typing import List


class Solution:

    def dfs(self,current_node,visited,graph,color):
        visited[current_node] = color

        for adj_node in graph[current_node] :
            if visited[adj_node] != -1 :

                if visited[adj_node] == color :
                    return False
            
            else :
                ans = self.dfs(adj_node,visited,graph,1-color)
                if ans is False :
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        visited = [-1 for _ in range(n)]

        for index in range(0,n):
            if visited[index] == -1 :
                ans = self.dfs(index,visited,graph,0)
                if ans is False :
                    return False

        return True