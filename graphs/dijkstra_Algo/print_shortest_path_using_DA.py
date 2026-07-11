import heapq
import sys
class Solution:
    def Sortestpath(self, n,edges,m):
        
        adj_list = [[] for _ in range(n+1)]
        for u,v,d in edges:
            adj_list[u].append([v,d])
            adj_list[v].append([u,d])

        priority_queue = [[0,1]]

        distance = [sys.maxsize for _ in range(n+1)]
        parent = [i for i in range(n+1)]
        distance[1] = 0

        # O(E log V)

        while len(priority_queue) != 0 :
            dist , node = heapq.heappop(priority_queue)

            if dist > distance[node]:
                continue

            for adjNode ,weight in adj_list[node]:
                new_d = weight + dist 
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d
                    heapq.heappush(priority_queue,[new_d,adjNode])
                    parent[adjNode] = node

        if distance[n] == sys.maxsize :
            return -1

        path = []
        node = n

        #  O(V)
        while parent[node] != node :
            path.append(node)
            node = parent[node]

        path.append(1)
        #  O(V)
        path.reverse()

        return path

s = Solution()
edges =[[1,2,2],[2,5,5],[2,3,4],[1,4,1],[4,3,3],[3,5,1]]
# total time complexity : O( E log V + 2V)
print(s.Sortestpath(5, edges, 6))
