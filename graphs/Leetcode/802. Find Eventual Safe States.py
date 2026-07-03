"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

from typing import List
from collections import deque


class Solution:
    
    def dfs(self, current_node, visited, graph):
    
        if visited[current_node] == 1:
            return False
        if visited[current_node] == 2:
            return True
        
        visited[current_node] = 1
        for neighbor in graph[current_node]:
            if not self.dfs(neighbor, visited, graph):
                return False
        
        visited[current_node] = 2
        return True 

    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = [0] * len(graph) 
        result = []
       
        for i in range(len(graph)):
            if visited[i] == 2 or self.dfs(i, visited, graph):
                result.append(i)

        return result  

# using BFS and kahn's algorithm 


class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n
        adj_reversed = [[] for _ in range(n)]
        
        # Step 1: Build the reversed graph and track out-degrees
        for i in range(n):
            for neighbor in graph[i]:
                adj_reversed[neighbor].append(i)
            out_degree[i] = len(graph[i])
            
        # Step 2: Push all terminal nodes (out-degree 0) into the queue
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n
        
        # Step 3: Process the queue
        while queue:
            node = queue.popleft()
            safe[node] = True
            
            for neighbor in adj_reversed[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 4: Return all safe nodes in sorted order
        return [i for i in range(n) if safe[i]]
