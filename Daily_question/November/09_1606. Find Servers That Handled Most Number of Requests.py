from sortedcontainers import SortedList # type: ignore
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        available = SortedList(range(k))
        busy_server = []
        mp = {}

        n = len(arrival)

        for i in range(n):

            while busy_server and busy_server[0][0] <= arrival[i]:
                free_time, server_id = heapq.heappop(busy_server)
                available.add(server_id)

            if not available:
                continue

            pos = i % k
            index = available.bisect_left(pos)

            if index == len(available):
                index = 0

            server_id = available[index]
            available.pop(index)

            mp[server_id] = mp.get(server_id, 0) + 1

            heapq.heappush(
                busy_server,
                (arrival[i] + load[i], server_id)
            )

        maxi = max(mp.values())

        return [
            server_id
            for server_id, count in mp.items()
            if count == maxi
        ]
