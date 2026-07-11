import heapq

class Solution:

    def dijkstra(self, V, edges, src):

        adj_list = [[] for _ in range(V)]

        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        distance = [float("inf")] * V
        distance[src] = 0

        priority_queue = [[0, src]]

        while priority_queue:

            dis, node = heapq.heappop(priority_queue)

            if dis > distance[node]:
                continue

            for adjNode, weight in adj_list[node]:
                new_d = dis + weight
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d
                    heapq.heappush(priority_queue, [new_d, adjNode])

        return distance