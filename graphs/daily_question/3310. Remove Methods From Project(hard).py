from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    
        adj_list =[[] for _ in range(n)]
        for u,v in invocations:
            adj_list[u].append(v)

        suspicious = [False]*n 
        def dfs(current_node,suspicious):
            if suspicious[current_node] is True :
                return 
            suspicious[current_node] = True 

            for adjNode in adj_list[current_node]:
                dfs(adjNode,suspicious)

            return 

        dfs(k, suspicious)

 
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
                
        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans

"""
Time Complexity
Build graph → O(E)
DFS → O(V + E)
Scan edges → O(E)
Build answer → O(V)
"""