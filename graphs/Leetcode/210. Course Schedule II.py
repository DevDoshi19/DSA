from collections import deque
from typing import List

"""
To succeed with this problem, you must always look out for three common pitfalls:
## 1. Direction of the Dependency

* The Catch: LeetCode defines the pairs as [course, prerequisite].
* The Fix: To take course A, you must finish course B first. This means your arrow must point from B -> A (adj[B].append(A)). Always read the problem description carefully to see which element points to which.

## 2. Cycle Detection

* The Catch: Deadlocks can happen (e.g., A needs B, and B needs A).
* The Fix:
* In BFS (Kahn's): If there is a cycle, those nodes will never hit an in-degree of 0 and will never enter the queue. Always check if len(result) == numCourses.
   * In DFS: You must use three states (unvisited, visiting, visited) to catch back-edges.

## 3. Disconnected Components

* The Catch: Some courses have absolutely no prerequisites, or the graph is split into separate, independent clusters.
* The Fix: Ensure your initial loop checks every single course from 0 to numCourses - 1 to find all starting points with 0 in-degree. Do not just loop through the pairs present in the input array.

Would you like me to show you an example input with a cycle to see exactly how the corrected code handles it?


"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]

        for u,v in prerequisites :
            adj_list[v].append(u)
            indeg[u] +=1 

        queue = deque()

        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)

        result = []
        while len(queue) :
            node = queue.popleft()
            result.append(node)
            for i in adj_list[node]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    queue.append(i)

        if len(result) == numCourses :
            return result

        return []
    
# using DFS 
class Solution1:
    
    def dfs(self,current_node,visited,adj_list,stack):
        visited[current_node] = 2
        for adjNode in adj_list[current_node]:
            if visited[adjNode] == 2 :
                return False

            if visited[adjNode] == 0:
                ans = self.dfs(adjNode,visited,adj_list,stack)
                if ans is False :
                    return False 

        visited[current_node] = 1
        stack.append(current_node)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        stack = []

        for u,v in prerequisites :
            adj_list[v].append(u) 

        for i in range(len(visited)):
            if visited[i] == 0 :
                if not self.dfs(i,visited,adj_list,stack) :
                    return []
                    
        if len(stack) == numCourses :
            return stack[::-1]

        return []