"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
# solution 1  - Kahn's algorithm (BFS)
from typing import List
from collections import deque

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for u,v in prerequisites :
            adj_list[u].append(v)
            indegree[v] += 1 

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        process_course = 0
        while len(queue) :
            node = queue.popleft()
            process_course +=1
            for i in adj_list[node] :
                indegree[i] -= 1
                if indegree[i] == 0 :
                    queue.append(i)

        return process_course==numCourses


# solution 2 - DFS which is similar to detecting cycle in directed graph but here we are using single visited variable instead of two visited and path visited variable.
# it will take to tle as the time complexity is O(n^2) in worst case as we are using adjacency list and for each node we are traversing all the adjacent nodes.
class Solution1:
    def dfs(self, current_node: int, visited: List[int], adj_list: List[List[int]]) -> bool:
        # State 1: Currently visiting (cycle detected)
        visited[current_node] = 1 
        
        for adjNode in adj_list[current_node]:
            if visited[adjNode] == 1:
                return False
            # Only recurse if the node hasn't been visited at all
            if visited[adjNode] == 0:
                if not self.dfs(adjNode, visited, adj_list):
                    return False
                
        # State 2: Fully processed and safe
        visited[current_node] = 2
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        # 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0 for _ in range(numCourses)]

        # Note: Usually prerequisites [u, v] means v must be taken before u (v -> u).
        # Building u -> v works identically for cycle detection purposes.
        for u, v in prerequisites:
            adj_list[u].append(v)

        for i in range(numCourses):
            if visited[i] == 0:
                if not self.dfs(i, visited, adj_list): 
                    return False

        return True

